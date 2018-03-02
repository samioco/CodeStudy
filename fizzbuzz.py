def fizzbuzz(n):
  output=""
  for i in range(1,n): 
    
    if i%3==0 and i%5==0:
      output+= "FizzBuzz" + "(" + str(i) + ")" + ", "
    elif i%3==0:
      output += "Fizz" + "(" + str(i) + ")" + ", "
    elif i%5==0:
      output += "Buzz" + "(" + str(i) + ")" + ", "
    else:
      output += str(i)+", "
    i+=1
  
  output=output.strip()
  if output[-1]==",": output=output[:-1]
  print output
  return



def main (argv):
  fizzbuzz(31)
  
  
  
if __name__ == "__main__":
  main(sys.argv[1:])
  