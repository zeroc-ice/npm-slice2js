#!/usr/bin/env node
//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

'use strict';

var compile = require('../index').compile;
compile(process.argv.slice(2), {stdio: 'inherit'}).on('exit', process.exit);
