// DOM Elements
const player = document.getElementById('mainPlayer');
const lessonTitle = document.getElementById('lessonTitle');
const lessonDesc = document.getElementById('lessonDescription');
const lessonDuration = document.getElementById('lessonDuration');
const playlistContainer = document.getElementById('playlistContainer');
const courseTitle = document.getElementById('courseTitle');
const instructorName = document.getElementById('instructorName');

// Initialize Player
function initPlayer() {
    //Populate Course Info from JSON
    if (courseData) {
        courseTitle.innerText = courseData.title;
        instructorName.innerText = courseData.instructor;
        
        renderPlaylist();
        
        // Auto-load the first lesson of the first module
        if(courseData.modules.length > 0 && courseData.modules[0].lessons.length > 0) {
            loadLesson(courseData.modules[0].lessons[0]);
        }
    }
}

// Render the Sidebar (Modules & Lessons)
function renderPlaylist() {
    playlistContainer.innerHTML = '';

    courseData.modules.forEach((module, modIndex) => {
        // Create Module Header
        const modDiv = document.createElement('div');
        modDiv.className = 'module-header';
        modDiv.innerHTML = `
            <span>${module.title}</span>
            <i class="fa-solid fa-chevron-down"></i>
        `;
        playlistContainer.appendChild(modDiv);

        // Create Lesson List
        const ul = document.createElement('ul');
        ul.className = 'lesson-list';
        
        module.lessons.forEach((lesson) => {
            const li = document.createElement('li');
            li.className = 'lesson-item';
            
            // Click Event to Switch Video
            li.onclick = () => {
                // Remove active class from all
                document.querySelectorAll('.lesson-item').forEach(i => i.classList.remove('active'));
                // Add active class to clicked
                li.classList.add('active');
                // Load video
                loadLesson(lesson);
            };

            li.innerHTML = `
                <i class="fa-regular fa-circle-play status-icon"></i>
                <div class="lesson-info">
                    <h4>${lesson.title}</h4>
                    <span><i class="fa-regular fa-clock"></i> ${lesson.duration}</span>
                </div>
            `;
            ul.appendChild(li);
        });

        playlistContainer.appendChild(ul);
    });
}

// Load Video Function
function loadLesson(lesson) {
    // Update Video Source
    player.src = `https://www.youtube-nocookie.com/embed/${lesson.video_id}?autoplay=1&rel=0`;
    
    // Update Text Details
    lessonTitle.innerText = lesson.title;
    lessonDesc.innerText = lesson.desc || "No description available for this lesson.";
    lessonDuration.innerText = lesson.duration;
}

// Start the player
initPlayer();