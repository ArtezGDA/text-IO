#!/usr/bin/env ruby

$:.unshift File.join(File.dirname(__FILE__), *%w[.. lib])

require 'yodaism'

Yodaism::Command.execute(*ARGV)