//  SaSS Watch static/scss -> static/css
module.exports = function(grunt) {
    // Project config
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        // Metadata
        meta: {
            basePath: '.',
            srcPath: './app/static/scss/',
            deployPath: './app/static/_css/'
        },

        banner: '/*! <%= pkg.name %> - v<%= pkg.version %> - ' +
                '<%= grunt.template.today("yyyy-mm-dd") %>\n' +
                '* Copyright (c) <%= grunt.template.today("yyyy") %> ',

        // Task config
        sass: {
            dist: {
                files: {
                    '<%= meta.deployPath %>_main.css' : '<%= meta.srcPath %>main.scss',
                    '<%= meta.deployPath %>_cover.css' : '<%= meta.srcPath %>cover.scss',
                    '<%= meta.deployPath %>_signin.css' : '<%= meta.srcPath %>signin.scss',
                    '<%= meta.deployPath %>_index.css' : '<%= meta.srcPath %>index.scss',
                    '<%= meta.deployPath %>_lock.css' : '<%= meta.srcPath %>lock.scss'
                }
            }
        },

        watch: {
            scripts: {
                files: [
                    '<%= meta.srcPath %>/**/*.scss'
                ],
                tasks: ['sass']
            }
        }
    });
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task
    grunt.loadNpmTasks('default', ['sass']);
    grunt.registerTask('default', ['watch']);
};
