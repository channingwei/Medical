# Medical Terminology Learning Platform

An interactive web application for learning medical terminology through flashcards, quizzes, and matching games.

## Features

- **Interactive Flashcards**: Study medical terms with flip-to-reveal functionality
- **Multiple Choice Quiz**: Test your knowledge with dynamic quiz generation
- **Matching Game**: Drag-and-drop matching of terms with their meanings
- **Chapter Organization**: Study by Prefixes, Suffixes, Root Words, and Variants
- **Progress Tracking**: Monitor your learning progress
- **Responsive Design**: Works on desktop and mobile devices

## Data

The application includes 1000 medical terms organized by type:
- **20 Prefixes**: a-, ab-, ad-, ante-, anti-, auto-, brady-, dys-, endo-, epi-, ex-, hemi-, hyper-, hypo-, in-, inter-, intra-, macro-, micro-, neo-
- **20 Suffixes**: -algia, -cele, -cyte, -ectomy, -emia, -itis, -logy, -lysis, -megaly, -oma, -pathy, -phobia, -plasia, -plasty, -rrhage, -rrhea, -sclerosis, -scopy, -stomy, -tomy
- **30 Root Words**: cardi/o, gastr/o, neur/o, dermat/o, oste/o, hepat/o, enter/o, pulmon/o, cyt/o, cephal/o, and more
- **930 Variants**: Additional variations and combinations

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Medical-Terminology
   ```

2. **Install Python dependencies**:
   ```bash
   pip3 install flask
   ```

3. **Run the application**:
   ```bash
   python3 app.py
   ```

4. **Open your browser** and go to:
   ```
   http://localhost:5001
   ```

## Usage

### Homepage
- View statistics of total terms, chapters, and root words
- Access all learning tools
- Browse all terms by chapter

### Flashcards
- Click on cards to flip and reveal meanings
- Navigate between cards with Previous/Next buttons
- Mark cards as correct/incorrect for progress tracking
- Filter by chapter or study all terms

### Quiz
- Multiple choice questions with 4 answer options
- Real-time scoring and feedback
- Chapter-specific or comprehensive quizzes
- Progress tracking and final results

### Matching Game
- Drag-and-drop interface to match terms with meanings
- Visual feedback for correct/incorrect matches
- Timer and scoring system
- Chapter selection and game reset

## Project Structure

```
Medical Terminology/
├── app.py                          # Main Flask application
├── data/
│   └── unique_1000_medical_word_parts.json  # Medical terms data
├── templates/
│   ├── index.html                  # Homepage
│   ├── flashcards.html             # Flashcards interface
│   ├── quiz.html                   # Quiz interface
│   └── match.html                  # Matching game interface
├── static/                         # Static assets (CSS, JS, images)
├── .gitignore                      # Git ignore rules
└── README.md                       # Project documentation
```

## API Endpoints

- `GET /` - Homepage
- `GET /flashcards` - Flashcards interface
- `GET /quiz` - Quiz interface
- `GET /match` - Matching game interface
- `GET /api/terms` - JSON API for medical terms data

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5
- **Icons**: Font Awesome
- **Data**: JSON format

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test the application
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- User accounts and progress saving
- Spaced repetition algorithm
- Audio pronunciation
- More comprehensive medical terminology database
- Mobile app version
- Export progress reports 