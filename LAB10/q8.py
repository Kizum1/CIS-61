(define (substitute s old new)
  ; YOUR-CODE-HERE
  (if (null? s)
      s
      (if (equal? (car s) old) 
          (cons new (substitute (cdr s) old new ))
          (cons (car s) (substitute (cdr s) old new))
          )
      )
  ) 