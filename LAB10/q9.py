(define (sub-all s olds news)

 (if (null? olds)
     s
     (sub-all (substitute s (car olds) (car news) ) (cdr olds) (cdr news)))
)