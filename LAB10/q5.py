(define (composed f g) 
(define (x y)
  (f (g x)))
 x
)
