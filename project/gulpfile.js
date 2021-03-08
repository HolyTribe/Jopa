//main
const gulp = require('gulp');
const replace = require('gulp-replace');

//Помощь при разработке
//Обновляет браузер, позволяет открывать проект на мобилке
const browserSync = require('browser-sync').create();

const header = require('gulp-header');

//JS

const webpack = require('webpack');
const webpackStream = require('webpack-stream');

const named = require('vinyl-named');
const uglify = require('gulp-uglify-es').default;

//CSS
const sass = require('gulp-sass');
const autoprefixer = require('gulp-autoprefixer');

//sprite
//Объединяет свг в спрайт
const svgSprite = require('gulp-svg-sprite');
//Удаляет лишние атры у свг
const cheerio = require('gulp-cheerio');


// Определяем логику работы Browsersync
function browsersync(done) {
    browserSync.init({
        notify: false, //Отключаем уведомления
        proxy: "localhost:8000" //Перенаправляем на джангу
    });
    done()
}

//Таск отвечающий за преобразование стилей
function cssTask(done) {
    gulp.src([
        'src/css/pages/*.scss'
    ]) // Получаем список нужных файлов
        .pipe(header('@import \'src/css/mixins\';\n')) //пахнет костылем, но оно добавляет миксины на все страницы
        .pipe(autoprefixer())
        .pipe(sass({
            outputStyle: 'compressed', //Сжимаем
            errorLogToConsole: true, //Вывод ошибок
        }))
        .on('error', console.log.bind(console)) //привязка к консоли
        .pipe(autoprefixer({overrideBrowserslist: ['last 2 versions'], cascade: false})) //Ставит автопрефиксы
        .pipe(gulp.dest('static/css/pages/')) // Помещаем в данную папку
    done()
}

//Слушатель событий
function watchTask(done) {
    browsersync(done);
    gulp.watch('src/css/**/*.scss', cssTask); //Вызывает функцию cssTask, если scss файл изменился
    gulp.watch('src/js/**/*.js', jsTask); //Вызывает функцию js, если js файл изменился
    gulp.watch('**/*.{scss,js,html}').on('change', browserSync.reload); //Смотрим изменения и перезагружаем браузер
    done()
}

function jsTask(done) {
    gulp.src([
        'src/js/pages/*.js',
        'src/js/tags/*.js'
    ])
        .pipe(named()) //Сохраняем название точек
        .pipe(webpackStream({
            mode: "development",
            output: {
                filename: "[name].js",
                path: __dirname + '.',
            },
            module: {
                rules: [
                    {
                        exclude: /node_modules/, //runtime ищет не там где надо
                        use: {
                            loader: 'babel-loader',
                            options: {
                                presets: ['@babel/preset-env'],
                                plugins: [
                                    ['@babel/plugin-proposal-class-properties'],
                                    ['@babel/plugin-transform-runtime'],
                                ]
                            }
                        }
                    },
                ],
            },
        }), webpack)
        .pipe(uglify()) //Убираем переносы
        .on('error', function () {
            this.emit('end');
        })
        .pipe(gulp.dest('static/js/pages/'))
    done()
}

function svgTask(done) {
    gulp.src('src/images/*.svg')
        .pipe(cheerio({
            run: function ($) {
                $("[fill]").removeAttr("fill");
                $("[clip]").removeAttr("clip");
                $("[stroke]").removeAttr("stroke");
                $("[mask]").removeAttr("mask");
                $("[opacity]").removeAttr("opacity");
                $("[width]").removeAttr("width");
                $("[height]").removeAttr("height");
                $("[class]").removeAttr("class");
            },
            parserOptions: {
                xmlMode: true
            }
        }))
        // У cheerio есть один баг — иногда он преобразовывает символ '>' в кодировку '&gt;'.
        .pipe(replace("&gt;", ">"))
        .pipe(svgSprite({
                mode: {
                    stack: {
                        sprite: "../sprite.svg"  //sprite file name
                    }
                },
            }
        ))
        .pipe(gulp.dest('static/images/'));
    done()
}


gulp.task('default', gulp.parallel(cssTask, jsTask, svgTask, watchTask))