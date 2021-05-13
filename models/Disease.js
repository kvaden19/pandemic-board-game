const { Model, DataTypes } = require('sequelize');
const sequelize = require('../config/connection');

class Disease extends Model {}

Disease.init(
  {
    id: {
      type: DataTypes.INTEGER,
      allowNull: false,
      primaryKey: true,
      autoIncrement: true,
    },
    color: {
      type: DataTypes.STRING
    },
    cubes: {
      type: DataTypes.INTEGER
    },
    cured: {
      type: DataTypes.BOOLEAN
    },
    eradicated: {
        type: DataTypes.BOOLEAN
    }
  },
  {
    sequelize,
    timestamps: false,
    freezeTableName: true,
    underscored: true,
    modelName: 'disease'
  }
);

module.exports = Disease;