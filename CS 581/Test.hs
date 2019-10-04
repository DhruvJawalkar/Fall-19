module Test where

sumtorial :: Int -> Int
sumtorial 0 = 0
sumtorial n = n + sumtorial (n-1)

data Expr
  = Lit Int
  | Add Expr Expr
  | Mul Expr Expr
  deriving (Eq,Show)

-- | The expression: 2 + 3 * 4
e1 = Add (Lit 2) (Mul (Lit 3) (Lit 4))

eval :: Expr -> Int
eval (Lit n) = n
eval (Add x y) = eval x + eval y
eval (Mul x y) = eval x * eval y

leftLit :: Expr -> Int
leftLit (Lit x) = x
leftLit (Add x y) = leftLit x 
leftLit (Mul x y) = leftLit x

rightLit :: Expr -> Int
rightLit (Lit x) = x
rightLit (Add x y) = rightLit y 
rightLit (Mul x y) = rightLit y

maxLit :: Expr -> Int
maxLit (Lit x) = x
maxLit (Add x y) = max (maxLit x) (maxLit y) 
maxLit (Mul x y) = max (maxLit x) (maxLit y) 

toRPN :: Expr -> String
toRPN (Lit n) = show n
toRPN (Add x y) = (toRPN x) ++ " " ++ (toRPN y) ++ " +" 
toRPN (Mul x y) = (toRPN x) ++ " " ++ (toRPN y) ++ " *"

convertToInt :: String -> Int
convertToInt x = (read x :: Int)

fromRPN :: String -> Expr
fromRPN x = Lit (convertToInt x)