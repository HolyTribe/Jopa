//main
const gulp = require('gulp');

function testTask(done) {
    console.log('work')
    done()
}

gulp.task('default', gulp.parallel(testTask))