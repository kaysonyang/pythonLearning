name = "Eric"

print("Hello %s,would you like to learn some Python today?"% name)

name = "Albert Einstein"
msg = "A person who never made a mistake never tried anything new."
print("%s once said, \"%s\"" % (name, msg))


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[-1])

msgText = f"My first biycle was {bicycles[0].title()}"
print(msgText)

bicycle = bicycles.pop()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles))
print(len(bicycles))
