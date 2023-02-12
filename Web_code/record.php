<?php 
  include 'connect.php';
?>

<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  
  <!-- Bootstrap CSS -->

  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <title>DIDA Collection</title>

  <style> 
    body {
        background-color: #120f28;
    }

    #myProgress {
      width: 100%;
      background-color: grey;
      border-radius: 8px;
    }

    #myBar {
      width: 0%;
      height: 6px;
      background-color: #fffae3;
      border-radius: 8px 2px 2px 8px;
      box-shadow: 1px 0 30px #fff;
    }

    .glow {
      color: #fffae3;
      text-shadow: #fff 1px 0 30px;
      font-family: Garamond, serif;
      text-align: center;
    }

    .center {
      display: block;
      margin-left: auto;
      margin-right: auto;
    } 

  </style>

</head>

<body>

  <div class="container">

    <div class="tab-content">
      <div id="home" class="tab-pane fade in active">

        <div id="collectTitle">
          <br><br>
          <h1 class="glow">即食予集點</h1>
          <h4 class="glow">DIDA Collection</h4>
          <br>
        </div>
        <!-- Progress Bar -->
        <div id="myProgress">
          <div id="myBar"></div>
        </div>
        <br>
        <?php 
          $amount = 400;
          $percentage = ($amount / 720) * 100;
        ?>
        <h4 class="glow">已捐贈額度：<?php echo $amount?></h4>
        <script>
          var i = 0;
          document.addEventListener("DOMContentLoaded", function(event) { 
            //do work
            if (i == 0) {
              i = 1;
              var elem = document.getElementById("myBar");
              var width = 1;
              var id = setInterval(addWidth, 20);

              function addWidth() {
                if (width >= <?php echo $percentage?>) {
                  clearInterval(id);
                  i = 0;
                } else {
                  width++;
                  elem.style.width = width + "%";
                }
              }
            }              
          });
        </script>
      </div>
    </div>
  </div>
  <img src="src/pic5.png" alt="Collection" width="400" height="450" class="center">
  <img src="src/share.png" alt="Record" id="record" hidden>
  <h4 id="share" class="glow"></h4>
  
  <script>
    const button = document.querySelector('#share');
    const img =  document.querySelector('#record');

    // Feature detection
    const supported = 'canShare' in navigator;
    // Update the button action text
    button.textContent = supported ? 'Share Record' : 'Download Record';

    const shareOrDownload = async (blob, fileName, title, text, url) => {
      // Using the Web Share API
      if (supported) {
        const data = {
          files: [
            new File([blob], fileName, {
              type: blob.type,
            }),
          ],
          title,
          text,
          url
        };
        if (navigator.canShare(data)) {
          try {
            await navigator.share(data);
          } catch (err) {
            if (err.name !== 'AbortError') {
              console.error(err.name, err.message);
            }
          } finally {
            return;
          }
        }
      }
      // Fallback implementation.
      const a = document.createElement('a');
      a.download = fileName;
      a.style.display = 'none';
      a.href = URL.createObjectURL(blob);
      a.addEventListener('click', () => {
        setTimeout(() => {
          URL.revokeObjectURL(a.href);
          a.remove();
        }, 1000)
      });
      document.body.append(a);
      a.click();
    };

    button.addEventListener('click', async () => {
      const blob = await fetch(img.src).then(res => res.blob());
      await shareOrDownload(blob, 'myCollection.png', 'DIDA Collection', '想要三個胖子嗎？一起來即食予集點！！', 'https://liff.line.me/1645278921-kWRPP32q/?accountId=195dceee');
    });
  </script>

</body>
</html>