(define (filter-lst f lst)

(if (null? lst)
     lst
     (if (f (car lst))
          (cons (car lst) (filter f (cdr lst)))
          (filter f (cdr lst))))
)


;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)
