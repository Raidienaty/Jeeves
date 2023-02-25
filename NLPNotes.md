# Natural Language Processing Notes

## Sentiment Analysis
Evaluates content to be either positive or negative. This results with a score and a magnitude value.
<br>
`Score` is bounded by -1.0 and 1.0. -1.0 corresponds to a negative content while 1.0 corresponds to a positive content. This score is the overall emotion covering the entire document. Strictly speaking, a document can contain sentence that are overall higher than the score and lower than the document score.
<br>
`Magnitude` is bounded by 0.0 and not bounded with an upper bound. Due to magnitude not being normalized, a larger text block will result in a larger magnitude.
<br>
Documents that recieve a score around 0.0 generally will dictate the document is possibly mixed emotion or neutral emotion. To distiguish this, the magnitude value will be higher on average for mixed emotion documents. On the other hand, neutral emotion documennts will result with low magnitude values and score.

## Entity Analysis
