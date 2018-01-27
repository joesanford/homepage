PDFJS.getDocument('static/joe_sanford.pdf').promise
    .then(function (pdf) {
        pdf.getPage(1)
    .then(function(page) {
        var scale = 1.5;
        var viewport = page.getViewport(scale);

        var canvas = document.getElementById('resume-canvas');
        var context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        var renderContext = {
            canvasContext: context,
            viewport: viewport
        };

        page.render(renderContext)
            .then(function () {
                pdf.getPage(2)
            .then(function (page) {
                var scale = 1.5;
                var viewport = page.getViewport(scale);

                var canvas = document.getElementById('resume-canvas2');
                var context = canvas.getContext('2d');
                canvas.height = viewport.height;
                canvas.width = viewport.width;

                var renderContext = {
                    canvasContext: context,
                    viewport: viewport
                };

                page.render(renderContext)
                    .then(function () {
                });
            });
        });
    });
}, function (error) {
    console.error(error);
});