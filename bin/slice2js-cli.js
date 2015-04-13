#!/usr/bin/env node
// **********************************************************************
//
// Copyright (c) 2003-2015 ZeroC, Inc. All rights reserved.
//
// **********************************************************************

'use strict';

var slice2js = require('../slice2js');
slice2js.compile(process.argv.slice(2), {stdio: 'inherit'}).on('exit', process.exit);
