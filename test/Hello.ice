//
// Copyright (c) ZeroC, Inc. All rights reserved.
//

#pragma once

module Demo
{

interface Hello
{
    idempotent void sayHello(int delay);
    void shutdown();
};

};
