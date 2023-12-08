import numpy as np 
import pandas as pd 
import werpy
from pyscript import document
 
def word_error_rate(event):
    input_text_reference = document.querySelector("#reference")
    input_text_hypothesis = document.querySelector("#hypothesis")
    reference = input_text_reference.value
    hypothesis = input_text_hypothesis.value

    ref_normalized = werpy.normalize(reference)
    hyp_normalized = werpy.normalize(hypothesis)
    
    output_div = document.querySelector("#output")
    output_div.innerText = werpy.wer(ref_normalized, hyp_normalized)
