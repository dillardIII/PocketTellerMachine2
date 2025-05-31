module.exports = {
    run: function (creep) {
        let ally = creep.pos.findClosestByRange(FIND_MY_CREEPS, {
            filter: (ally) => ally.hits < ally.hitsMax
        });
        if (ally) {
            if (creep.heal(ally) === ERR_NOT_IN_RANGE) {
                creep.moveTo(ally, { visualizePathStyle: { stroke: '#00ff00' } });
            }
        } else {
            creep.moveTo(Game.flags.Medbay, { visualizePathStyle: { stroke: '#00ff00' } });
        }
    }
};