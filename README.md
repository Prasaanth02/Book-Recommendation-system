# 📚 Book Recommendation System

A colorful, interactive web application that recommends books based on your current mood. Built with HTML, CSS, and JavaScript.

**[🌐 Try the Live Demo](https://prasaanth02.github.io/Book-Recommendation-System/)** - Experience the application directly in your browser!

![Book Recommendation System](https://raw.githubusercontent.com/Prasaanth02/Book-Recommendation-System/main/screenshots/main_screen.png)

## Features

- **Mood-Based Recommendations**: Get personalized book recommendations based on 7 different moods
- **Interactive UI**: Colorful, user-friendly interface with visual feedback and animations
- **Save Favorites**: Save books you're interested in for later reference
- **Rate Books**: Rate your saved books on a 5-star scale
- **Local Storage**: Your saved books and ratings are stored in your browser
- **Data Export/Import**: Easily backup and restore your saved books
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Moods and Color Themes

The system offers recommendations based on these moods, each with its own color theme:

- **Happy 😊** - Yellow/Gold theme
- **Sad 😢** - Blue theme
- **Excited 🤩** - Orange/Red theme
- **Relaxed 😌** - Green theme
- **Curious 🧐** - Purple theme
- **Adventurous 🧗** - Teal theme
- **Inspired ✨** - Pink theme

## How to Use

### Online Version
The easiest way to use the Book Recommendation System is through the online version:

**[🌐 Access the Book Recommendation System](https://Prasaanth02.github.io/Book-Recommendation-System/)**

This version runs directly in your browser with no installation required!

### Local Installation
If you prefer to run the application locally:

1. Clone this repository or download the source code
```bash
git clone https://github.com/Prasaanth02/Book-Recommendation-System.git
```

2. Navigate to the project directory
```bash
cd Book-Recommendation-System
```

3. Open the `index.html` file in your web browser

## Using the Application

1. **Get Recommendations**:
   - Select your current mood from the buttons at the top
   - View the recommended books that match your mood
   - Each mood displays 5 different book recommendations

2. **Save Books**:
   - Click the "Save This Book" button on any book you're interested in
   - Your saved books are stored in your browser's local storage

3. **View Saved Books**:
   - Click "My Saved Books 🔖" in the top right corner
   - See all your saved books in one place

4. **Rate Books**:
   - In the saved books view, rate any book from 1 to 5 stars
   - Hover over the stars to see a preview of your rating
   - Click to confirm your rating

5. **Remove Books**:
   - Remove any book from your saved collection using the "Remove" button

6. **Manage Your Data**:
   - Click the "⚙️ Settings" button in the top right corner
   - Export your data as a JSON file for backup
   - Import previously exported data
   - Clear all data if needed

## Data Storage

The application stores your saved books and ratings in your browser's local storage:

- **Privacy**: Your data never leaves your device
- **Persistence**: Your saved books remain available even after closing the browser
- **Limitations**: Clearing your browser data will also clear your saved books
- **Backup**: Use the Export/Import feature in Settings to backup your data

## Book Database

The system includes 35 books (5 for each mood) covering various genres:
- Fiction and fantasy
- Non-fiction and memoirs
- Science and philosophy
- Adventure and travel
- Self-help and personal development

## Technical Details

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Storage**: Browser Local Storage API
- **Design**: Responsive design with CSS Grid and Flexbox
- **Fonts**: Google Fonts (Roboto)

## Browser Compatibility

The application works on all modern browsers:
- Google Chrome (recommended)
- Mozilla Firefox
- Microsoft Edge
- Safari
- Opera

## Customization

Developers can easily extend the book database by modifying the `booksDatabase` object in `script.js`. Each book requires:
- Title
- Author
- Description

## Future Enhancements

- Add book cover images
- Implement search functionality
- Connect to external book APIs for more recommendations
- Add user accounts for cloud synchronization
- Implement dark mode
- Add social sharing features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Book descriptions and recommendations inspired by popular literature
- Color themes designed for optimal mood association
- UI design focused on user experience and visual appeal

---

## Get Help & Support

Having trouble with the Book Recommendation System? Here's how to get help:

1. **Check the README** - Most common questions are answered in this document
2. **Contact the Developer** - Email me at [prasaanthhari02@gmail.com](mailto:prasaanthhari02@gmail.com)
3. **Report Issues** - If you find a bug, please report it by [creating an issue](https://github.com/Prasaanth02/Book-Recommendation-System/issues)

---

Created by [Prasaanth](https://github.com/Prasaanth02) - 2025

**[🌐 Try the Book Recommendation System Now!](https://prasaanth02.github.io/Book-Recommendation-System/)**