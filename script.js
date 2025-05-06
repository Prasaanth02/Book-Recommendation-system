// Book database organized by mood
const booksDatabase = {
    "Happy 😊": [
        {"title": "The Alchemist", "author": "Paulo Coelho", "description": "A magical story about following your dreams."},
        {"title": "A Man Called Ove", "author": "Fredrik Backman", "description": "A heartwarming tale about the transformative power of friendship."},
        {"title": "The House in the Cerulean Sea", "author": "TJ Klune", "description": "A charming fantasy novel full of joy and found family."},
        {"title": "Where the Crawdads Sing", "author": "Delia Owens", "description": "A beautiful coming-of-age story set in the marshes of North Carolina."},
        {"title": "Project Hail Mary", "author": "Andy Weir", "description": "An uplifting sci-fi adventure about saving humanity."}
    ],
    "Sad 😢": [
        {"title": "A Little Life", "author": "Hanya Yanagihara", "description": "A profound exploration of trauma, friendship, and healing."},
        {"title": "The Road", "author": "Cormac McCarthy", "description": "A post-apocalyptic tale of a father and son's journey."},
        {"title": "Never Let Me Go", "author": "Kazuo Ishiguro", "description": "A melancholic story about love and what it means to be human."},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "description": "A nostalgic story of loss and growing up."},
        {"title": "The Book Thief", "author": "Markus Zusak", "description": "A poignant tale set during World War II, narrated by Death."}
    ],
    "Excited 🤩": [
        {"title": "Ready Player One", "author": "Ernest Cline", "description": "A thrilling adventure in a virtual reality world."},
        {"title": "The Hunger Games", "author": "Suzanne Collins", "description": "A fast-paced dystopian adventure of survival."},
        {"title": "Jurassic Park", "author": "Michael Crichton", "description": "A thrilling sci-fi adventure with dinosaurs."},
        {"title": "The Da Vinci Code", "author": "Dan Brown", "description": "A page-turning mystery filled with codes and conspiracies."},
        {"title": "Artemis Fowl", "author": "Eoin Colfer", "description": "An exciting tale of a young criminal mastermind."}
    ],
    "Relaxed 😌": [
        {"title": "The Thursday Murder Club", "author": "Richard Osman", "description": "A cozy mystery solved by retirement home residents."},
        {"title": "Under the Tuscan Sun", "author": "Frances Mayes", "description": "A memoir about renovating a villa in Tuscany."},
        {"title": "The No. 1 Ladies' Detective Agency", "author": "Alexander McCall Smith", "description": "Gentle mysteries set in Botswana."},
        {"title": "A Year in Provence", "author": "Peter Mayle", "description": "A charming account of life in the French countryside."},
        {"title": "The Secret Garden", "author": "Frances Hodgson Burnett", "description": "A classic tale of renewal and growth."}
    ],
    "Curious 🧐": [
        {"title": "Sapiens", "author": "Yuval Noah Harari", "description": "A brief history of humankind."},
        {"title": "Freakonomics", "author": "Steven D. Levitt & Stephen J. Dubner", "description": "Exploring the hidden side of everything."},
        {"title": "Cosmos", "author": "Carl Sagan", "description": "A journey through the universe."},
        {"title": "The Code Breaker", "author": "Walter Isaacson", "description": "The story of CRISPR and gene editing."},
        {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "description": "An exploration of the two systems that drive the way we think."}
    ],
    "Adventurous 🧗": [
        {"title": "Into Thin Air", "author": "Jon Krakauer", "description": "A personal account of the Mt. Everest disaster."},
        {"title": "The Lost City of Z", "author": "David Grann", "description": "A tale of deadly obsession in the Amazon."},
        {"title": "Endurance", "author": "Alfred Lansing", "description": "Shackleton's incredible voyage in Antarctica."},
        {"title": "Wild", "author": "Cheryl Strayed", "description": "A woman's journey of self-discovery on the Pacific Crest Trail."},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A classic adventure of a hobbit's unexpected journey."}
    ],
    "Inspired ✨": [
        {"title": "Educated", "author": "Tara Westover", "description": "A memoir about the transformative power of education."},
        {"title": "Becoming", "author": "Michelle Obama", "description": "The former First Lady's inspiring journey."},
        {"title": "Atomic Habits", "author": "James Clear", "description": "Building good habits and breaking bad ones."},
        {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "description": "Finding purpose and meaning in difficult circumstances."},
        {"title": "The Power of Now", "author": "Eckhart Tolle", "description": "A guide to spiritual enlightenment."}
    ]
};

// Mood colors mapping
const moodColors = {
    "Happy 😊": {"primary": "#FFD700", "secondary": "#FFEB99", "text": "#8B4513"},
    "Sad 😢": {"primary": "#6495ED", "secondary": "#B0C4DE", "text": "#00008B"},
    "Excited 🤩": {"primary": "#FF4500", "secondary": "#FFA07A", "text": "#8B0000"},
    "Relaxed 😌": {"primary": "#98FB98", "secondary": "#DCFCDC", "text": "#006400"},
    "Curious 🧐": {"primary": "#9370DB", "secondary": "#D8BFD8", "text": "#4B0082"},
    "Adventurous 🧗": {"primary": "#20B2AA", "secondary": "#AFEEEE", "text": "#008080"},
    "Inspired ✨": {"primary": "#FF69B4", "secondary": "#FFC0CB", "text": "#8B008B"}
};

// DOM Elements
const moodButtons = document.querySelectorAll('.mood-btn');
const welcomeView = document.getElementById('welcomeView');
const recommendationsView = document.getElementById('recommendationsView');
const savedBooksView = document.getElementById('savedBooksView');
const booksContainer = document.getElementById('booksContainer');
const savedBooksContainer = document.getElementById('savedBooksContainer');
const noSavedBooks = document.getElementById('noSavedBooks');
const savedBooksBtn = document.getElementById('savedBooksBtn');
const settingsBtn = document.getElementById('settingsBtn');
const settingsModal = document.getElementById('settingsModal');
const closeSettingsBtn = document.getElementById('closeSettingsBtn');
const clearDataBtn = document.getElementById('clearDataBtn');
const exportDataBtn = document.getElementById('exportDataBtn');
const importDataBtn = document.getElementById('importDataBtn');
const getRecommendationsBtn = document.getElementById('getRecommendationsBtn');
const moodRecommendationTitle = document.getElementById('moodRecommendationTitle');
const recommendationsHeader = document.getElementById('recommendationsHeader');

// Current state
let currentView = 'welcome';
let selectedMood = null;
let savedBooks = [];

// Initialize the application
function init() {
    loadSavedBooks();
    setupEventListeners();
}

// Load saved books from local storage
function loadSavedBooks() {
    const savedData = localStorage.getItem('bookRecommendationData');
    if (savedData) {
        savedBooks = JSON.parse(savedData);
    }
}

// Save books to local storage
function saveBooksToStorage() {
    localStorage.setItem('bookRecommendationData', JSON.stringify(savedBooks));
}

// Setup event listeners
function setupEventListeners() {
    // Mood button click events
    moodButtons.forEach(button => {
        button.addEventListener('click', () => {
            const mood = button.getAttribute('data-mood');
            selectMood(mood, button);
        });
    });

    // Navigation button events
    savedBooksBtn.addEventListener('click', showSavedBooksView);
    settingsBtn.addEventListener('click', showSettingsModal);
    closeSettingsBtn.addEventListener('click', hideSettingsModal);
    getRecommendationsBtn.addEventListener('click', showRecommendationsView);

    // Settings modal events
    document.querySelector('.close-btn').addEventListener('click', hideSettingsModal);
    clearDataBtn.addEventListener('click', clearAllData);
    exportDataBtn.addEventListener('click', exportData);
    importDataBtn.addEventListener('click', importData);

    // Close modal when clicking outside
    window.addEventListener('click', (e) => {
        if (e.target === settingsModal) {
            hideSettingsModal();
        }
    });
}

// Select a mood and show recommendations
function selectMood(mood, clickedButton) {
    // Reset previous selection
    moodButtons.forEach(btn => btn.classList.remove('selected'));
    
    // Set new selection
    clickedButton.classList.add('selected');
    selectedMood = mood;
    
    // Show recommendations
    showRecommendations(mood);
}

// Show recommendations for selected mood
function showRecommendations(mood) {
    // Update view
    currentView = 'recommendations';
    welcomeView.classList.add('hidden');
    recommendationsView.classList.remove('hidden');
    savedBooksView.classList.add('hidden');
    
    // Clear previous recommendations
    booksContainer.innerHTML = '';
    
    // Update header
    const moodName = mood.split(' ')[0];
    moodRecommendationTitle.textContent = `📚 Based on your ${moodName.toLowerCase()} mood, we recommend these books: 📚`;
    
    // Apply mood-specific styling to header
    const colors = moodColors[mood];
    recommendationsHeader.style.backgroundColor = colors.secondary;
    recommendationsHeader.style.color = colors.text;
    
    // Display books
    const books = booksDatabase[mood];
    books.forEach((book, index) => {
        const bookCard = createBookCard(book, index + 1, mood);
        booksContainer.appendChild(bookCard);
    });
}

// Create a book card element
function createBookCard(book, number, mood) {
    const colors = moodColors[mood];
    
    const bookCard = document.createElement('div');
    bookCard.className = 'book-card';
    
    const colorBar = document.createElement('div');
    colorBar.className = 'book-color-bar';
    colorBar.style.backgroundColor = colors.primary;
    
    const bookContent = document.createElement('div');
    bookContent.className = 'book-content';
    
    const bookNumber = document.createElement('span');
    bookNumber.className = 'book-number';
    bookNumber.textContent = `Book ${number}`;
    bookNumber.style.backgroundColor = colors.primary;
    
    const bookTitle = document.createElement('h3');
    bookTitle.className = 'book-title';
    bookTitle.textContent = `📕 ${book.title}`;
    bookTitle.style.color = colors.text;
    
    const bookAuthor = document.createElement('p');
    bookAuthor.className = 'book-author';
    bookAuthor.textContent = `by ${book.author} ✍️`;
    
    const bookDescription = document.createElement('div');
    bookDescription.className = 'book-description';
    bookDescription.textContent = `💬 ${book.description}`;
    bookDescription.style.backgroundColor = colors.secondary;
    bookDescription.style.color = colors.text;
    
    const saveBtn = document.createElement('button');
    saveBtn.className = 'save-btn';
    saveBtn.textContent = '🔖 Save This Book';
    saveBtn.style.backgroundColor = colors.primary;
    
    // Add hover effect
    saveBtn.addEventListener('mouseenter', () => {
        saveBtn.style.backgroundColor = colors.text;
    });
    
    saveBtn.addEventListener('mouseleave', () => {
        saveBtn.style.backgroundColor = colors.primary;
    });
    
    // Save book functionality
    saveBtn.addEventListener('click', () => {
        saveBook(book, mood);
    });
    
    // Assemble the card
    bookContent.appendChild(bookNumber);
    bookContent.appendChild(bookTitle);
    bookContent.appendChild(bookAuthor);
    bookContent.appendChild(bookDescription);
    bookContent.appendChild(saveBtn);
    
    bookCard.appendChild(colorBar);
    bookCard.appendChild(bookContent);
    
    return bookCard;
}

// Save a book
function saveBook(book, mood) {
    // Check if book is already saved
    const isAlreadySaved = savedBooks.some(savedBook => 
        savedBook.title === book.title && savedBook.author === book.author
    );
    
    if (isAlreadySaved) {
        alert(`'${book.title}' is already in your saved books!`);
        return;
    }
    
    // Add book to saved books
    const savedBook = {
        ...book,
        mood: mood,
        rating: 0
    };
    
    savedBooks.push(savedBook);
    saveBooksToStorage();
    alert(`'${book.title}' has been added to your saved books!`);
}

// Show saved books view
function showSavedBooksView() {
    currentView = 'savedBooks';
    welcomeView.classList.add('hidden');
    recommendationsView.classList.add('hidden');
    savedBooksView.classList.remove('hidden');
    
    displaySavedBooks();
}

// Show recommendations view
function showRecommendationsView() {
    if (selectedMood) {
        showRecommendations(selectedMood);
    } else {
        currentView = 'welcome';
        welcomeView.classList.remove('hidden');
        recommendationsView.classList.add('hidden');
        savedBooksView.classList.add('hidden');
    }
}

// Display saved books
function displaySavedBooks() {
    savedBooksContainer.innerHTML = '';
    
    if (savedBooks.length === 0) {
        savedBooksContainer.classList.add('hidden');
        noSavedBooks.classList.remove('hidden');
        return;
    }
    
    savedBooksContainer.classList.remove('hidden');
    noSavedBooks.classList.add('hidden');
    
    savedBooks.forEach((book, index) => {
        const bookCard = createSavedBookCard(book, index + 1);
        savedBooksContainer.appendChild(bookCard);
    });
}

// Create a saved book card
function createSavedBookCard(book, number) {
    const bookCard = document.createElement('div');
    bookCard.className = 'saved-book-card';
    
    const bookHeader = document.createElement('div');
    bookHeader.className = 'saved-book-header';
    
    const bookNumberLabel = document.createElement('span');
    bookNumberLabel.className = 'book-number-label';
    bookNumberLabel.textContent = `Book ${number}`;
    
    const moodLabel = document.createElement('span');
    moodLabel.className = 'mood-label';
    moodLabel.textContent = `Mood: ${book.mood.split(' ')[0]}`;
    
    const bookTitle = document.createElement('h3');
    bookTitle.className = 'saved-book-title';
    bookTitle.textContent = `📕 ${book.title}`;
    
    const bookAuthor = document.createElement('p');
    bookAuthor.className = 'saved-book-author';
    bookAuthor.textContent = `by ${book.author} ✍️`;
    
    const bookDescription = document.createElement('div');
    bookDescription.className = 'saved-book-description';
    bookDescription.textContent = `💬 ${book.description}`;
    
    const bookActions = document.createElement('div');
    bookActions.className = 'book-actions';
    
    const ratingContainer = document.createElement('div');
    ratingContainer.className = 'rating-container';
    
    const ratingLabel = document.createElement('span');
    ratingLabel.className = 'rating-label';
    ratingLabel.textContent = 'Rate this book:';
    
    const stars = document.createElement('div');
    stars.className = 'stars';
    
    // Create 5 stars
    for (let i = 1; i <= 5; i++) {
        const star = document.createElement('span');
        star.className = 'star';
        star.textContent = '★';
        if (i <= book.rating) {
            star.classList.add('filled');
        }
        
        // Add rating functionality
        star.addEventListener('click', () => {
            rateBook(book.title, i);
        });
        
        // Add hover effects
        star.addEventListener('mouseenter', () => {
            // Highlight stars up to this one
            const allStars = stars.querySelectorAll('.star');
            allStars.forEach((s, index) => {
                if (index < i) {
                    s.style.color = '#ffaa00';
                } else {
                    s.style.color = '#dddddd';
                }
            });
        });
        
        star.addEventListener('mouseleave', () => {
            // Restore original state
            const allStars = stars.querySelectorAll('.star');
            allStars.forEach((s, index) => {
                if (index < book.rating) {
                    s.style.color = '#ffcc00';
                } else {
                    s.style.color = '#dddddd';
                }
            });
        });
        
        stars.appendChild(star);
    }
    
    const removeBtn = document.createElement('button');
    removeBtn.className = 'remove-btn';
    removeBtn.textContent = '🗑️ Remove';
    removeBtn.addEventListener('click', () => {
        removeBook(book.title);
    });
    
    // Assemble the card
    bookHeader.appendChild(bookNumberLabel);
    bookHeader.appendChild(moodLabel);
    
    ratingContainer.appendChild(ratingLabel);
    ratingContainer.appendChild(stars);
    
    bookActions.appendChild(ratingContainer);
    bookActions.appendChild(removeBtn);
    
    bookCard.appendChild(bookHeader);
    bookCard.appendChild(bookTitle);
    bookCard.appendChild(bookAuthor);
    bookCard.appendChild(bookDescription);
    bookCard.appendChild(bookActions);
    
    return bookCard;
}

// Rate a book
function rateBook(title, rating) {
    const bookIndex = savedBooks.findIndex(book => book.title === title);
    if (bookIndex !== -1) {
        savedBooks[bookIndex].rating = rating;
        saveBooksToStorage();
        alert(`You rated '${title}' ${rating}/5 stars!`);
        displaySavedBooks();
    }
}

// Remove a book
function removeBook(title) {
    const bookIndex = savedBooks.findIndex(book => book.title === title);
    if (bookIndex !== -1) {
        savedBooks.splice(bookIndex, 1);
        saveBooksToStorage();
        alert(`'${title}' has been removed from your saved books.`);
        displaySavedBooks();
    }
}

// Show settings modal
function showSettingsModal() {
    settingsModal.classList.remove('hidden');
}

// Hide settings modal
function hideSettingsModal() {
    settingsModal.classList.add('hidden');
}

// Clear all data
function clearAllData() {
    if (confirm('Are you sure you want to clear all your saved books? This action cannot be undone.')) {
        savedBooks = [];
        saveBooksToStorage();
        alert('All data has been cleared.');
        
        if (currentView === 'savedBooks') {
            displaySavedBooks();
        }
    }
}

// Export data
function exportData() {
    const dataStr = JSON.stringify(savedBooks, null, 2);
    const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
    
    const exportFileDefaultName = 'book_recommendations_data.json';
    
    const linkElement = document.createElement('a');
    linkElement.setAttribute('href', dataUri);
    linkElement.setAttribute('download', exportFileDefaultName);
    linkElement.click();
}

// Import data
function importData() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    
    input.onchange = e => {
        const file = e.target.files[0];
        const reader = new FileReader();
        
        reader.onload = event => {
            try {
                const data = JSON.parse(event.target.result);
                if (Array.isArray(data)) {
                    savedBooks = data;
                    saveBooksToStorage();
                    alert('Data imported successfully!');
                    
                    if (currentView === 'savedBooks') {
                        displaySavedBooks();
                    }
                } else {
                    alert('Invalid data format. Please import a valid JSON file.');
                }
            } catch (error) {
                alert('Error importing data: ' + error.message);
            }
        };
        
        reader.readAsText(file);
    };
    
    input.click();
}

// Initialize the application
document.addEventListener('DOMContentLoaded', init);