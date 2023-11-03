import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: MovieListScreen(),
    );
  }
}

class MovieListScreen extends StatefulWidget {
  @override
  _MovieListScreenState createState() => _MovieListScreenState();
}

class _MovieListScreenState extends State<MovieListScreen> {
  List<Movie> movies = [];
  Movie? selectedMovie;
  int ticketCount = 0;

  @override
  void initState() {
    super.initState();
    fetchMovies();
  }

  Future<void> fetchMovies() async {
    final Uri url = Uri.https('api.themoviedb.org', '/3/discover/movie', {
      'sort_by': 'popularity.desc',
      'api_key': 'fa3e844ce31744388e07fa47c7c5d8c3',
    });

    final response = await http.get(url);
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      final results = data['results'];
      List<Movie> movieList = [];
      for (var result in results) {
        movieList.add(Movie.fromJson(result));
      }
      setState(() {
        movies = movieList;
      });
    }
  }

  void addToCart() {
    if (selectedMovie != null) {
      setState(() {
        ticketCount++;
      });
    }
  }

  void removeFromCart() {
    if (ticketCount > 0) {
      setState(() {
        ticketCount--;
      });
    }
  }

  void confirmPurchase() {
    if (selectedMovie != null) {
      final totalPrice = ticketCount * 30; // Precio por entrada de 30 Bs
      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => MoviePurchaseSummary(
            movie: selectedMovie!,
            ticketCount: ticketCount,
            totalPrice: totalPrice,
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Lista de Películas')),
      body: ListView.builder(
        itemCount: movies.length,
        itemBuilder: (context, index) {
          final movie = movies[index];
          return ListTile(
            leading: Image.network(
              'https://image.tmdb.org/t/p/w185${movie.posterPath}',
              width: 50, // Ajusta el tamaño de la imagen según tus necesidades
            ),
            title: Text(movies[index].title),
            subtitle: Text(movies[index].overview),
            onTap: () {
              setState(() {
                selectedMovie = movies[index];
                ticketCount = 0;
              });
            },
          );
        },
      ),
      bottomNavigationBar: BottomAppBar(
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            IconButton(
              icon: Icon(Icons.add),
              onPressed: addToCart,
            ),
            Text('Entradas: $ticketCount'),
            IconButton(
              icon: Icon(Icons.remove),
              onPressed: removeFromCart,
            ),
            ElevatedButton(
              onPressed: confirmPurchase,
              child: Text('Confirmar Compra'),
            ),
          ],
        ),
      ),
    );
  }
}

class MoviePurchaseSummary extends StatelessWidget {
  final Movie movie;
  final int ticketCount;
  final int totalPrice;

  MoviePurchaseSummary(
      {required this.movie,
      required this.ticketCount,
      required this.totalPrice});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Resumen de Compra')),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Título: ${movie.title}'),
            Text('Entradas: $ticketCount'),
            Text('Precio total: $totalPrice Bs'),
          ],
        ),
      ),
    );
  }
}

class Movie {
  final String title;
  final String overview;
  final String posterPath; // Agregamos una propiedad para la ruta del póster

  Movie(
      {required this.title, required this.overview, required this.posterPath});

  factory Movie.fromJson(Map<String, dynamic> json) {
    return Movie(
      title: json['title'],
      overview: json['overview'],
      posterPath:
          json['poster_path'], // Utiliza la propiedad del póster de la API
    );
  }
}
