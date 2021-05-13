// const Disease = require('./Disease');
// const sequelize = require('../config/connection');

// //module.exports = { Disease };

// // const testDatabase = async () => {
// //     await sequelize.sync({ force: true });
  
// //     let disease = await Disease.create({color: 'red', cubes: 96, cured: true, eradicated: false});
// //     console.log(disease);
  
// //     process.exit(0);
// // };
  
// // testDatabase();

// sequelize.sync({ force: false }).then(() => {
//     console.log('Hello from model/index.js');
// });

const sequelize = require('../config/connection');

sequelize.sync({ force: false }).then(() => {
  console.log('Hello from model/index.js');
});