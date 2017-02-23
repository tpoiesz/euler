lineso = do
	content <- readFile "euler013"
	return (lines content)

readLines [] = []
readLines (x:xs) = (read x) : (readLines xs)

run = do
	content <- readFile "euler013"
	let stringLines = lines content
	let intLines = readLines stringLines
	print (sum intLines)
