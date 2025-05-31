module.exports = {
    run: function (creep) {
        let target = creep.pos.findClosestByPath(FIND_HOSTILE_CREEPS);
        if (target) {
            if (creep.attack(target) === ERR_NOT_IN_RANGE) {
                creep.moveTo(target, { visualizePathStyle: { stroke: '#ff0000' } });
            }
        } else {
            creep.moveTo(Game.flags.Battle, { visualizePathStyle: { stroke: '#ff0000' } });
        }
    }
};