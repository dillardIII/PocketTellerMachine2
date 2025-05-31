module.exports = {
    run: function (creep) {
        if (!creep.memory.explored) {
            let exits = Game.map.describeExits(creep.room.name);
            for (let dir in exits) {
                if (Game.rooms[exits[dir]]) continue;
                creep.moveTo(new RoomPosition(25, 25, exits[dir]));
                return;
            }
            creep.memory.explored = true;
        } else {
            creep.moveTo(Game.flags.Scout);
        }
    }
};