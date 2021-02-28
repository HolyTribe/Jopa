//main
const gulp = require('gulp');

//Помощь при разработке
const browserSync = require('browser-sync').create();


// Определяем логику работы Browsersync
function browsersync() {
	browserSync.init({ // Инициализация Browsersync
		server: { baseDir: '/' }, // Указываем папку сервера
		notify: false, // Отключаем уведомления
		online: true // Режим работы: true или false
	})
}

function testTask(done) {
    console.log('work')
    done()
}

gulp.task('default', browsersync)