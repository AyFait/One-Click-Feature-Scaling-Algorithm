#THIS IS A PREPROCESSING STAGE/STEP

#CAN BE USED BEFORE OF AFTER PRINCIPAL COMPONENT ANALYSIS (PCA): which reduces number of features

#It advised to use this before PCA though


>Skips the yTrain Col
>
>Skips categorical cols cus they are known to have close range of values (optional)
>
>Skips cols with close/small range of values (optional)
>
>Target for small range of vals
>
>

#Methods:

#DIV BY MAX
>	elmt = elmt / max
>
>	print range of values (min to max)
 
#MEAN NORM
>	get avg
>
>	elmt = (elmt - avg) / (max - min)
>
>	print range of values (min to max)
	
#Z-SCORE NORM
>	get stdDev
>
>	get avg
>
>	elmt = (elmt - avg) / stdDev
>
>	print range of values (min to max)
