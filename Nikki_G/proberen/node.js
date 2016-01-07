    var sys = require('sys');
    var colors = require('colors'); // colors are fun!
    var translate = require('./lib/translate');

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