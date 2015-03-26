// **********************************************************************
//
// Copyright (c) 2003-2015 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************
//
// Ice version 3.6.0
//
// <auto-generated>
//
// Generated from file `Hello.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>
//

(function(module, require, exports)
{
    var Ice = require("zeroc-icejs").Ice;
    var __M = Ice.__M;
    var Slice = Ice.Slice;

    var Demo = __M.module("Demo");

    Demo.Hello = Slice.defineObject(
        undefined,
        Ice.Object, undefined, 0,
        [
            "::Demo::Hello",
            "::Ice::Object"
        ],
        -1, undefined, undefined, false);

    Demo.HelloPrx = Slice.defineProxy(Ice.ObjectPrx, Demo.Hello.ice_staticId, undefined);

    Slice.defineOperations(Demo.Hello, Demo.HelloPrx,
    {
        "sayHello": [, 2, 2, , , , [[3]], , , , ],
        "shutdown": [, , , , , , , , , , ]
    });
    exports.Demo = Demo;
}
(typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? module : undefined,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? require : window.Ice.__require,
 typeof(global) !== "undefined" && typeof(global.process) !== "undefined" ? exports : window));
