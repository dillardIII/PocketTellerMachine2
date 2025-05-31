// === Main Screeps Loop ===

const roleHarvester = require('role.harvester');
const roleUpgrader = require('role.upgrader');
const roleBuilder = require('role.builder');
const roleSoldier = require('role.soldier');
const roleHealer = require('role.healer');
const roleScout = require('role.scout');

module.exports.loop = function () {
    for (let name in Memory.creeps) {
        if (!Game.creeps[name]) {
            delete Memory.creeps[name];
        }
    }

    for (let name in Game.creeps) {
        let creep = Game.creeps[name];
        if (creep.memory.role === 'harvester') {
            roleHarvester.run(creep);
        } else if (creep.memory.role === 'upgrader') {
            roleUpgrader.run(creep);
        } else if (creep.memory.role === 'builder') {
            roleBuilder.run(creep);
        } else if (creep.memory.role === 'soldier') {
            roleSoldier.run(creep);
        } else if (creep.memory.role === 'healer') {
            roleHealer.run(creep);
        } else if (creep.memory.role === 'scout') {
            roleScout.run(creep);
        }
    }
};