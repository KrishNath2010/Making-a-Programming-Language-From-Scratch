let rec fac x = 
  if x = 0 then 1 else 
    x * fac(x - 1);;
let rec makefact num l =
  if num = 10 then l else 
    makefact (num + 1) (l @ [(num * (List.nth l (num - 1)))]) 
let fac_list = makefact 1 [1] 
let rec  sum_of_factorial_of_digits index number_list =
  if index < (List.length number_list) - 1 then sum_of_factorial_of_digits (index + 1)  number_list + List.nth fac_list (List.nth number_list index) else
    List.nth fac_list (List.nth number_list index)
let rec make_number_list num num_list =
  if num <= 0 then num_list else 
    make_number_list (num / 10) ([(num mod 10)] @ num_list) ;; 
let main (num: int) : int = if ((sum_of_factorial_of_digits 0 (make_number_list num [])) == num) then num else 0 ;; 
let check (i: int) : int = if (main i) == i then i else 0 ;; 
for i = 1 to 10000000 do if (check i)!=0 then print_endline (string_of_int i) done;;