import arena

arena.init("oz.andrew.cmu.edu", "realm", "hello")

arena.Object(
    objName="primordialDie1",
    objType=arena.Shape.cube,
    physics=arena.Physics.dynamic,
    location=(0, 5, 0),
    ttl=5
)


arena.handle_events()
