# swiss_encoder
The encoding swiss army knife for oneliner payloads.


##EXAMPLES:

### regular base64 
./swiss_encoder.py base64 hello world

aGVsbG8gd29ybGQ=

### url safe encoding 
./swiss_encoder.py url
paste your oneliner below:
hello~!@#$%^&*()_+=-,./<>?;':":[]{}|\`world

hello~%21%40%23%24%25%5E%26%2A%28%29_%2B%3D-%2C.%2F%3C%3E%3F%3B%27%3A%22%3A%5B%5D%7B%7D%7C%5C%60world


### based64 that works with that stupid windows utf-16 default encoding
./swiss_encoder.py win64
paste your oneliner below:
write-host hello; write-host world
powershell -e dwByAGkAdABlAC0AaABvAHMAdAAgAGgAZQBsAGwAbwA7ACAAdwByAGkAdABlAC0AaABvAHMAdAAgAHcAbwByAGwAZAA=
