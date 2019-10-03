module HW1 where


-- | A representation of arithmetic expressions as binary trees where leaves
--   are literal integers and internal nodes are either addition or
--   multiplaction nodes. Note that this data structure is an "abstract
--   syntax tree", which is something we will spend more time talking about
--   later in the course.
data Expr
   = Lit Int         -- ^ Literal integers
   | Add Expr Expr   -- ^ Addition expressions
   | Mul Expr Expr   -- ^ Multiplication expressions
  deriving (Eq,Show)


-- | The expression: 2 + 3 * 4
e1 :: Expr
e1 = Add (Lit 2) (Mul (Lit 3) (Lit 4))


-- | The expression: (7 + 6) * 5
e2 :: Expr
e2 = Mul (Add (Lit 7) (Lit 6)) (Lit 5)


-- | The expresssion: 3 * 2 + 5 * 4
e3 :: Expr
e3 = undefined


-- | The expression: 8 + 7 * 9 + 6
e4 :: Expr
e4 = undefined


-- | The leftmost literal in an expression.
--
--   >>> leftLit (Lit 3)
--   3
--
--   >>> leftLit e1
--   2
--   
--   >>> leftLit e2
--   7
--
leftLit :: Expr -> Int
leftLit = undefined


-- | The rightmost literal in an expression.
--
--   >>> rightLit (Lit 3)
--   3
--
--   >>> rightLit e3
--   4
--   
--   >>> rightLit e4
--   6
--
rightLit :: Expr -> Int
rightLit = undefined


-- | Get the maximum literal value in an expression.
--
--   >>> maxLit (Lit 3)
--   3
--
--   >>> maxLit e1
--   4
--
--   >>> maxLit e2
--   7
--
--   >>> maxLit e3
--   5
--
--   >>> maxLit e4
--   9
--
maxLit :: Expr -> Int
maxLit = undefined


-- | The integer result of evaluating an expression.
--
--   >>> eval (Lit 3)
--   3
--
--   >>> eval e1
--   14
--
--   >>> eval e2
--   65
--
--   >>> eval e3
--   26
--
--   >>> eval e4
--   77
--
eval :: Expr -> Int
eval = undefined
