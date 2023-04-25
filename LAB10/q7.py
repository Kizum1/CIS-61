(define (no-repeats s)
 'YOUR-CODE-HERE
 (if (null? s)
     s
     (cons (car s)
        (no-repeats (filter (lambda (x) (not (= x (car s)) ) ) (cdr s)) 
        ))
)
)

;;; Tests
(no-repeats (list 5 4 5 4 2 2))
; expect (5 4 2)