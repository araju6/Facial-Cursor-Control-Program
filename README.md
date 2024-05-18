<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Facial Mouse Control</h1>
    <p>This project enables users with physical impairments to operate a mouse cursor using facial movements and eye gestures. The program uses OpenCV for facial and eye detection, and the Win32 API for mouse control on Windows systems.</p>
    <h2>Features</h2>
    <ul>
        <li><strong>Cursor Movement</strong>: Move the mouse cursor by moving your face.</li>
        <li><strong>Left Click</strong>: Blink both eyes to perform a left click.</li>
        <li><strong>Right Click</strong>: Wink with one eye to perform a right click.</li>
    </ul>
    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.x</li>
        <li>OpenCV</li>
        <li>PyWin32</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/yourusername/facial-mouse-control.git
      
cd facial-mouse-control</code></pre>
        </li>
        <li><strong>Install the required packages:</strong>
            <pre><code>pip install opencv-python
pip install pywin32</code></pre>
        </li>
        <li><strong>Download Haar Cascades:</strong>
            <p>Ensure you have the Haar Cascade files:</p>
            <ul>
                <li><code>haarcascade_frontalface_default.xml</code></li>
                <li><code>haarcascade_eye_tree_eyeglasses.xml</code></li>
            </ul>
            <p>You can download these from the <a href="https://github.com/opencv/opencv/tree/master/data/haarcascades">OpenCV GitHub repository</a>.</p>
        </li>
    </ol>
    <h2>Usage</h2>
    <ol>
        <li><strong>Run the program:</strong>
            <pre><code>python facial_mouse_control.py</code></pre>
        </li>
        <li><strong>Instructions:</strong>
            <ul>
                <li>Position your face within the camera's view.</li>
                <li>Move your face to move the cursor.</li>
                <li>Blink both eyes to perform a left click.</li>
                <li>Wink with one eye to perform a right click.</li>
            </ul>
        </li>
    </ol>
    <h2>Notes</h2>
    <p>The program currently uses a simple method for cursor movement which may need adjustments based on your screen resolution and camera setup. Blink and wink detection might require calibration to work accurately for different users.</p>
    <p>Enjoy using the Facial Mouse Control program!</p>
</body>
</html>
