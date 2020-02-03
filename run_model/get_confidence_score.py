import math
import re
from joblib import load

import pandas as pd

from get_concavity_score import get_concavity_score
from get_all_ca_pos import get_all_ca_pos


def get_single_delta_ca(int_resnum_and_chain, int_ca_pos_dict,
                        ref_resnum_and_chain, ref_ca_pos_dict):
    """Get the change in alpha-carbon position of a single residue.

    The structures are referred to as the "structure of interest" and the
    "reference structure".  It doesn't matter which structure is which.

    Parameters
    ----------
    int_resnum_and_chain : string of form resnum:chain
        The residue number and chain of the structure of interest.
    int_ca_pos_dict : dictionary of form resnum_and_chain : position
        A dictionary of all alpha-carbon positions for the structure of interest.
        Values are lists of floats, [x_pos, y_pos, z_pos].
    ref_resnum_and_chain : string of form resnum:chain
        The residue number and chain of the reference structure.
    ref_ca_pos_dict : dictionary of form resnum_and_chain : position
        A dictionary of all alpha-carbon positions for the reference structure.
        Values are lists of floats, [x_pos, y_pos, z_pos].

    Returns
    -------
    delta_ca : float
        The distance of the selected alpha carbon between the 2 structures.

    """

    if (int_resnum_and_chain not in int_ca_pos_dict or
            ref_resnum_and_chain not in ref_ca_pos_dict):
        return 0
    int_pos = int_ca_pos_dict[int_resnum_and_chain]
    ref_pos = ref_ca_pos_dict[ref_resnum_and_chain]
    delta_ca = math.sqrt((int_pos[0] - ref_pos[0])**2 + (int_pos[1] - ref_pos[1])**2 +
                         (int_pos[2] - ref_pos[2])**2)
    return delta_ca


def get_confidence_score(pdb_file_loc, prot_name, output_dir, apo_conc_scores, apo_ca_pos_dict):
    """Get the ML confidence score of each residue in an MD snapshot being in an open pocket.

    The code refers to an "apo" structure.  This is the structure at/before the start of the
    MD simulation.

    Parameters
    ----------
    pdb_file_loc : string
        The path to the PDB file of the MD snapshot.  It should have chains listed in the
        Chain column; it is not sufficient for them te be listed in the Segid column.
    prot_name : string
        The name of the MD snapshot.  It should probably resemble pdb_file_loc.
    output_dir : string
        The name of the directory where the output is stored.
        If the directory already exists, its contents will be overwritten.
    apo_conc_scores : dictionary
        The concavity scores of the apo structure, as determined by get_concavity_score.
    apo_ca_pos_dict : dictionary
        The alpha carbon positions of the apo structure, as determined by get_all_ca_pos.

    Returns
    -------
    dict_res_to_score : dictionary
        The distance of the selected alpha carbon between the 2 structures.
        Keys are strings of the form resnum:chain.

    """

    concavity_scores = get_concavity_score(pdb_file_loc, prot_name, output_dir)
    ca_pos_dict = get_all_ca_pos(pdb_file_loc)
    delta_pos_dict = {}
    for resnum_and_chain, ca_pos in ca_pos_dict.items():
        # get_single_delta_ca allows for the resnum_and_chain to be different in the 2
        # structures.  But this isn't the case here, so resnum_and_chain gets passed
        # twice.
        delta_pos_dict[resnum_and_chain] = get_single_delta_ca(resnum_and_chain,
                                                               ca_pos_dict,
                                                               resnum_and_chain,
                                                               apo_ca_pos_dict)
    dataframe_as_list = []
    for resnum_and_chain, conc_score in concavity_scores.items():
        delta_conc_score = conc_score - apo_conc_scores[resnum_and_chain]
        delta_ca_pos = delta_pos_dict[resnum_and_chain]
        # FIXME warn if insertion code present.
        re_str_resnum_chain = "(.+):(.+)"
        re_search_resnum_chain = re.search(re_str_resnum_chain, resnum_and_chain)
        resnum = re_search_resnum_chain.group(1)
        chain = re_search_resnum_chain.group(2)
        try:
            resnum_minus = str(int(resnum) - 1)
        except ValueError:
            neighbor_conc_score = 0
            neighbor_delta_ca_pos = 0
            neighbor_delta_conc = 0
            continue
        resnum_minus_and_chain = "%s:%s" %(resnum_minus, chain)
        if resnum_minus_and_chain not in ca_pos_dict:
            has_minus = False
        else:
            has_minus = True
            neighbor_conc_minus = concavity_scores[resnum_minus_and_chain]
            neighbor_delta_ca_minus = delta_pos_dict[resnum_minus_and_chain]
            neighbor_delta_conc_minus = (neighbor_conc_minus -
                                         apo_conc_scores[resnum_minus_and_chain])
        resnum_plus = str(int(resnum) + 1)
        resnum_plus_and_chain = "%s:%s" %(resnum_plus, chain)
        if resnum_plus_and_chain not in ca_pos_dict:
            has_plus = False
        else:
            has_plus = True
            neighbor_conc_plus = concavity_scores[resnum_plus_and_chain]
            neighbor_delta_ca_plus = delta_pos_dict[resnum_plus_and_chain]
            neighbor_delta_conc_plus = neighbor_conc_plus - apo_conc_scores[resnum_plus_and_chain]
        if has_plus and (not has_minus):
            neighbor_conc_score = neighbor_conc_plus
            neighbor_delta_ca_pos = neighbor_delta_ca_plus
            neighbor_delta_conc = neighbor_delta_conc_plus
        elif has_minus and (not has_plus):
            neighbor_conc_score = neighbor_conc_minus
            neighbor_delta_ca_pos = neighbor_delta_ca_minus
            neighbor_delta_conc = neighbor_delta_conc_minus
        elif (not has_minus) and (not has_plus):
            neighbor_conc_score = 0
            neighbor_delta_ca_pos = 0
            neighbor_delta_conc = 0
        else:
            neighbor_conc_score = ((neighbor_conc_plus + neighbor_conc_minus) / 2)
            neighbor_delta_ca_pos = ((neighbor_delta_ca_plus + neighbor_delta_ca_minus) / 2)
            neighbor_delta_conc = ((neighbor_delta_conc_plus + neighbor_delta_conc_minus) / 2)
        dataframe_as_list.append([resnum_and_chain, conc_score, neighbor_conc_score,
                                  delta_conc_score, neighbor_delta_conc, delta_ca_pos,
                                  neighbor_delta_ca_pos])
    dataframe_as_df = pd.DataFrame(dataframe_as_list,
                                   columns=["resnum_and_chain", "conc_score",
                                            "neighbor_conc_score", "delta_conc_score",
                                            "neighbor_delta_conc", "delta_ca_pos",
                                            "neighbor_delta_ca_pos"])
    loaded_info = load("../train_model/ml/trained_model.joblib")
    pipeline = loaded_info["model"]
    included_columns = ["conc_score", "neighbor_conc_score",
                        "delta_conc_score", "neighbor_delta_conc", "delta_ca_pos",
                        "neighbor_delta_ca_pos"]
    X = dataframe_as_df[included_columns]
    probs = pipeline.predict_proba(X)[0:]
    scores_pos = []
    for score in probs:
        scores_pos.append(score[1])
    dataframe_as_df["predict_proba"] = scores_pos
    dict_res_to_score = {}
    for index, row in dataframe_as_df.iterrows():
        dict_res_to_score[row["resnum_and_chain"]] = row["predict_proba"]
    return dict_res_to_score
