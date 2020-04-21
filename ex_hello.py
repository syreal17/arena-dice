import arena
arena.init("oz.andrew.cmu.edu", "realm", "hello")
arena.Object(objType=arena.Shape.cube, ttl=7)
arena.handle_events()
