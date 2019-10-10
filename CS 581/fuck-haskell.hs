module FuckThisShit where
import Data.List
-- map processes every element in an array, applies a funtion to each element
-- (a -> b) -> [a] -> [b] 

zz  :: (a->b) -> [a] -> [b]
zz _ [] = []
zz f (x:xs) = f x : zz f xs

-- : cons operator, used to prepend head to a list
-- ++ appends 2 lists
-- since return type of reverse is a list cant use cons op,  my_reverse xs  : x : []
my_reverse :: [a] -> [a]
my_reverse [] = []
my_reverse (x:xs) = (my_reverse xs) ++ [x]

-- strings are double quotes, map (++ "!") ["bang", "pow"]

my_filter :: (a -> Bool) -> [a] -> [a]
my_filter _ [] = []
my_filter p (x:xs)
        | p x = x : my_filter p xs
        | otherwise = my_filter p xs

isEven :: Int -> Bool
isEven n = n `mod` 2==0

-- first checks for n, then evaluates clause 1 ..
-- guards are like if else conditions
-- `div` is for integer division
hailstone :: Int -> Int
hailstone n
      | n `mod` 2 ==0 = n `div` 2
      | n `mod` 3 ==0 = n `div` 3
      | otherwise = 3*n + 1 

intListLength :: [Int] -> Int
intListLength [] = 0
intListLength (x:xs) = 1 + intListLength xs       

lengthOfString :: [Char] -> Int
lengthOfString [] = 0
lengthOfString (x:xs) = 1 + lengthOfString xs

-- | Convert a regular list into a run-length list.
--
--   >>> compress [1,1,1,2,3,3,3,1,2,2,2,2]
--   [(3,1),(1,2),(3,3),(1,1),(4,2)]
-- 
--   >>> compress "Mississippi"
--   [(1,'M'),(1,'i'),(2,'s'),(1,'i'),(2,'s'),(1,'i'),(2,'p'),(1,'i')]
--

compress :: Eq a => [a] -> [(Int,a)]
--compress = map (\x -> (length x, head x)) . group
compress str = map (\x -> (length x, head x)) (group str)
--compress = [(length x, take 1 x) | x <- group]

decode :: Eq a => [(Int,a)] -> [a]
decode xs = foldr f [] xs
  where
    f (1, x) r = x : r
    f (k, x) r = x : f (k-1, x) r

decompress :: Eq a => [(Int,a)] -> [a]
decompress = concatMap (uncurry replicate)