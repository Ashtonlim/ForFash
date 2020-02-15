const path = require('path');
const common = require('./webpack.common');
const merge = require('webpack-merge');

module.exports = merge(common, {
    mode: 'development',
    devtool: 'inline-source-map',
    watch: true,
    output: {
        path: path.resolve(__dirname, 'ff/static/ff'),
        filename: 'main.js'
    }
});