n = 10000000
count = 0

for i in (1..n) do
  x = rand()*2-1
  y = rand()*2-1
  if (x*x+y*y < 1)
    count +=1
  end
end

printf("Pi is roughly %f", 4.0*count/n)
