#!/usr/bin/env node
//
// Copyright (c) ZeroC, Inc. All rights reserved.
//
//

var path     = require('path');
var slice2js = require('./../index');

var args = [];
args.push('test/Hello.ice');
args.push('--output-dir=test');

slice2js.compile(args, {stdio: 'inherit'}).on('close', function (code)
{
    process.exit(code);
});
