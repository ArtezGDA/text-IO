
/*
translate.js - node-demo.js
Copyright (c) 2010 Marak Squires
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

var sys = require('sys');
var colors = require('colors'); // colors are fun!
var translate = require('../lib/translate');

// TODO: make this demo automatically iterate through all langauges as a test instead of manually nesting only 3
    
// note: the translator is  English=>Spanish by default
translate.text('I want tacos please.', function(err, text){

  sys.puts('I want tacos please.'.red + ' => '.cyan + text.yellow);
  var input = 'Spanish', output = "Japanese";
  translate.text({input:input,output:output}, text, function(err, text2){

    var input = 'Japanese', output = "English";
    sys.puts(text.yellow + ' => '.cyan + text2.blue);
    translate.text({input:input,output:output}, text, function(err, text3){

       sys.puts(text2.blue + ' => '.cyan + text3.red);
       sys.puts('English'.red+'=>'+'Spanish'.yellow+'=>'+'Japanese'.blue+'=>'+'English'.red  +'\ntaco request has been normalized. ^_^'.green);
    });
  }); 
}); 