import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  Offset _offset = Offset(100, 100);
  double _width = 120.0;
  String url =
      "http://a4.att.hudong.com/15/94/50200014992522154424948721605_s.jpg";

  double x = 0.0;
  double y = 55.0;
  double initx = -1;
  Image img = Image.network(
      'https://p3-security.byteimg.com/img/security-captcha/slide_c4a3041656fd7651e57ea2bbb52c1bafa46ec4e1_1_1.jpg~tplv-obj.image');
  double w = 0;
  double h = 0;

  @override
  void initState() {
    img.image
        .resolve(new ImageConfiguration())
        .addListener(new ImageStreamListener(
          (ImageInfo info, bool _) {
            w = info.image.width.toDouble();
            h = info.image.height.toDouble();
            print("获取到宽度：$w 高度：$h");
//            completer.complete(Rect.fromLTWH(0, 0, info.image.width.toDouble(),
//                info.image.height.toDouble()));
          },
          onError: (dynamic exception, StackTrace stackTrace) {
            // completer.completeError(exception, stackTrace);
          },
        ));
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    print("width1:${MediaQuery.of(context).size}");
    return Scaffold(
      body: Center(
        child: Container(
//          width: w,
//          height: h,
          child: Stack(
            children: [
              img,
              Positioned(
                  // red box
                  child: Container(
                    child: GestureDetector(
                      child: Image.network(
                          'https://p3-security.byteimg.com/img/security-captcha/slide_c4a3041656fd7651e57ea2bbb52c1bafa46ec4e1_2_1.png~tplv-obj.image'),
                      onPanUpdate: (detail) {
                        print(
                            "被拖动,dx=${detail.delta.dx},dy=${detail.delta.dy},dex1=${detail.globalPosition.dx},dy1=${detail.globalPosition.dy},dx2=${detail.localPosition.dx},dx3=${detail.localPosition.dx}");
                        if (initx == -1) {
                          initx = detail.localPosition.dx;
                        }
                        print("width2:${MediaQuery.of(context).size}");
                        if (detail.localPosition.dx < initx || initx > w) {
                        } else {
                          setState(() {
                            x = detail.localPosition.dx;
                            //y = detail.globalPosition.dy;
                          });
                        }
                      },
                      onPanEnd: (detail) {
                        print("拖动结束了！");
                      },
                    ),
                  ),
                  left: x,
                  top: y),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
