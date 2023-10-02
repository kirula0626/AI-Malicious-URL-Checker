from urllib.parse import urlparse
import subprocess

# Function to extract URLs from a paragraph using urllib.parse
def extract_urls(paragraph):
    # Split the paragraph into words and check each word as a potential URL
    words = paragraph.split()
    urls = []
    for word in words:
        parsed_url = urlparse(word)
        if parsed_url.scheme and parsed_url.netloc:
            urls.append(word)
    return urls

# Predefined paragraph with various types of URLs

paragraph_with_urls = """
 
<tbody>
<tr>
<td style=  background-color:#ffffff  >
 
</tbody></table>
</td>
</tr>
</tbody>
</table>


<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border:0;border-collapse:collapse;border-spacing:0;margin:auto;max-width:700px  >
<tbody>
<tr>
<td align=  center  >
<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  background-color:#fff;border:0;border-collapse:collapse;border-spacing:0;margin:auto   bgcolor=  #ffffff  >
<tbody>
<tr>
<td align=  center  >

<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border:0;border-collapse:collapse;border-spacing:0  >
<tbody>
<tr>
<td align=  center   style=  background-color:#ffffff  >
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   style=  border:0;border-collapse:collapse;border-spacing:0  >
<tbody>
<tr>
<td>

<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border:0;border-collapse:collapse;border-spacing:0  >
<tbody>
<tr>
<td>

<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border:0;border-collapse:collapse;border-spacing:0  >
<tbody>
<tr>
<td>











  
<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
<tbody>


  

  
  
  

  
    
    
    
  

<tr>
  <td align=  left   style=  direction:ltr;text-align:left;background-color:#ffffff;padding:10px 14px 21px 14px  >
    <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
      <tbody>
        <tr>
          <td style=  direction:ltr;text-align:left  >
          
                  <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t10of12   align=  center   style=  Margin:0 auto;border-collapse:collapse;max-width:560px;width:100%  >
                    <tbody>
                      <tr>
                        <td style=  direction:ltr;text-align:left;padding-left:0;padding-right:0  >
                          <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                            <tbody>


  
  <tr>
    <td style=  direction:ltr;text-align:left;color:#000000;font-family:   Uber Move   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:24px;font-weight:500;line-height:30px;padding-bottom:7px;padding-left:12px;padding-right:12px;padding-top:7px  >
      Savings for you coming right up
    </td>
  </tr>

  <tr>
    <td style=  direction:ltr;text-align:left  >
    

        <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t5of12   align=  left   style=  border-collapse:collapse;max-width:374px;width:100%  >
          <tbody>
            <tr>
            
              <td width=  50%   style=  direction:ltr;text-align:left;padding-left:0;padding-right:0   valign=  top  >
                <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
                  <tbody>
                    <tr>
                      <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                        <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                          <tbody>
                            
                            
                            <tr>
                <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  Pancake Delight  >
                  
                
                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Df6041567-90ea-418b-b71a-68c08f039ccc&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fpancake-delight-malabe%2F9gQVZ5DqQYu3GmjAjwOczA&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D0   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Df6041567-90ea-418b-b71a-68c08f039ccc%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fpancake-delight-malabe%252F9gQVZ5DqQYu3GmjAjwOczA%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D0&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw2p8tGY_wyFkL_t79syz2AO  >
                <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
                <tbody>
                 <tr>
                 
                   <td style=  padding-top:8px;padding-bottom:50px  >
                    <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                     <tbody>
                      <tr>
                       <td style=  color:#ffffff;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:500;line-height:10px;background-color:#04c168;padding:4px 8px 4px 4px;border-radius:0 20px 20px 0  >
                       Buy 1, get 1 free
                       </td>
                      </tr>
                    </tbody></table>
                    </td>
                  </tr>
                  
                  
                  <tr>
                   <td align=  right   valign=  bottom   style=  vertical-align:bottom;padding:4px 4px 4px 4px  >
                    <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                     <tbody>
                      <tr>
                       <td style=  color:#000000;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:300;line-height:10px;background-color:#e0e0e0;padding:4px 4px 4px 4px;border-radius:10px 10px 10px 10px  >
                       4.6
                       </td>
                      </tr>
                    </tbody></table>
                    </td>
                  </tr>
                  
                </tbody>
                </table>
                </a>
                    
                  
                </td>
                </tr>
                            
                            <tr>
                              <td style=  direction:ltr;text-align:left;padding-bottom:4px  >
                                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Df6041567-90ea-418b-b71a-68c08f039ccc&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fpancake-delight-malabe%2F9gQVZ5DqQYu3GmjAjwOczA&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D0   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Df6041567-90ea-418b-b71a-68c08f039ccc%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fpancake-delight-malabe%252F9gQVZ5DqQYu3GmjAjwOczA%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D0&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw2p8tGY_wyFkL_t79syz2AO  >
                                  <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                   Pancake Delight
                                  </span>
                                  <br>
                                  <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                                    $$ • Drinks • Chinese
                                  </span>
                                  <br>
                                  <span style=  color:#036134;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    Order now →
                                  </span>
                                </a>
                              </td>
                            </tr>
                          
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>

              <td width=  50%   style=  direction:ltr;text-align:left;padding-left:0;padding-right:0   valign=  top  >
                <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
                  <tbody>
                    <tr>
                      <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                        <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                          <tbody>
                            
                            <tr>
                <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  Flames by Better Butter Bakery  >
                  
                
                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D7684c30a-3529-4092-bbe2-8f243ae75086&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fflames-by-better-butter-bakery-malabe%2FdoTDCjUpQJK74o8kOudQhg&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D0   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D7684c30a-3529-4092-bbe2-8f243ae75086%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fflames-by-better-butter-bakery-malabe%252FdoTDCjUpQJK74o8kOudQhg%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D0&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw3JWf-Lnjak1Ht_GHfGjRQi  >
                <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
                <tbody>
                 
                 <tr>
                   <td style=  padding-top:8px;padding-bottom:50px  >
                    <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                     <tbody>
                      <tr>
                       <td style=  color:#ffffff;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:500;line-height:10px;background-color:#04c168;padding:4px 8px 4px 4px;border-radius:0 20px 20px 0  >
                       Buy 1, get 1 free
                       </td>
                      </tr>
                    </tbody></table>
                    </td>
                  </tr>
                  
                  
                  <tr>
                   <td align=  right   valign=  bottom   style=  vertical-align:bottom;padding:4px 4px 4px 4px  >
                    <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                     <tbody>
                      <tr>
                       <td style=  color:#000000;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:300;line-height:10px;background-color:#e0e0e0;padding:4px 4px 4px 4px;border-radius:10px 10px 10px 10px  >
                       4.4
                       </td>
                      </tr>
                    </tbody></table>
                    </td>
                  </tr>
                  
                </tbody>
                </table>
                </a>
                    
                  
                </td>
                </tr>
                            <tr>
                              <td style=  direction:ltr;text-align:left;padding-bottom:4px  >
                                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D7684c30a-3529-4092-bbe2-8f243ae75086&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fflames-by-better-butter-bakery-malabe%2FdoTDCjUpQJK74o8kOudQhg&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D2%26ds_sp%3D0   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D7684c30a-3529-4092-bbe2-8f243ae75086%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fflames-by-better-butter-bakery-malabe%252FdoTDCjUpQJK74o8kOudQhg%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D2%2526ds_sp%253D0&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw0XjqDUcMWSFvCea9kBJtpj  >
                                  <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    Flames by Better Butter Bakery
                                  </span>
                                  <br>
                                  <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                                    $ • Bakery • Desserts
                                  </span>
                                  <br>
                                  <span style=  color:#036134;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    Order now →
                                  </span>
                                </a>
                              </td>
                            </tr>
                            
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>

            </tr>
          </tbody>
        </table>

         

         
         <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t1of12 m_5925240524307192452thirdwheel   align=  left   style=  border-collapse:collapse;max-width:186px;width:100%  >
            <tbody>
              <tr>
                <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                  <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                    <tbody>
                      
                      <tr>
            <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  New Pubudu Hotel  >
              
            
            <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D8acd60c5-8f0b-4379-a151-8727b74cd32b&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fnew-pubudu-hotel-talawatugoda%2Fis1gxY8LQ3mhUYcnt0zTKw&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D0   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D8acd60c5-8f0b-4379-a151-8727b74cd32b%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fnew-pubudu-hotel-talawatugoda%252Fis1gxY8LQ3mhUYcnt0zTKw%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D0&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw07WYXhLNCzxrKGP8FF5jAw  >
            <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
              <tbody>
               
               <tr>
               <td style=  padding-top:8px;padding-bottom:50px  >
                <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                   <tbody>
                  <tr>
                     <td style=  color:#ffffff;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:500;line-height:10px;background-color:#04c168;padding:4px 8px 4px 4px;border-radius:0 20px 20px 0  >
                     Spend LKR&nbsp;1,000, save LKR&nbsp;250
                     </td>
                  </tr>
                  </tbody></table>
                </td>
              </tr>
              
              
              <tr>
                <td align=  right   valign=  bottom   style=  vertical-align:bottom;padding:4px 4px 4px 4px  >
                   <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                    <tbody>
                     <tr>
                      <td style=  color:#000000;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:300;line-height:10px;background-color:#e0e0e0;padding:4px 4px 4px 4px;border-radius:10px 10px 10px 10px  >
                      4.6
                      </td>
                     </tr>
                   </tbody></table>
                   </td>
                 </tr>
                 
            </tbody>
            </table>
            </a>
                
              
            </td>
            </tr>
                      <tr>
                        <td style=  direction:ltr;text-align:left;padding-bottom:4px  >
                          <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D8acd60c5-8f0b-4379-a151-8727b74cd32b&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fnew-pubudu-hotel-talawatugoda%2Fis1gxY8LQ3mhUYcnt0zTKw&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D3%26ds_sp%3D0   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D8acd60c5-8f0b-4379-a151-8727b74cd32b%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fnew-pubudu-hotel-talawatugoda%252Fis1gxY8LQ3mhUYcnt0zTKw%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D3%2526ds_sp%253D0&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw3q79H3Z8KrvuxZMCrFIDqW  >
                            <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                              New Pubudu Hotel
                            </span> <br>
                            <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                              $ • Sri Lankan • Drinks
                            </span><br>
                            <span style=  color:#036134;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                              Order now →
                            </span>
                          </a>
                        </td>
                      </tr>
                      
                    </tbody>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        

        
  </td>
</tr>





                              </tbody>
                            </table>
                          </td>
                        </tr>
                    </tbody>
                  </table>
                
          </td>
        </tr>
      </tbody>
    </table>
  </td>
</tr>





  

  
  
  

  
    
    
    
  

<tr>
  <td align=  left   style=  direction:ltr;text-align:left;background-color:#ffffff;padding:10px 14px 21px 14px  >
    <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
      <tbody>
        <tr>
          <td style=  direction:ltr;text-align:left  >
          
                  <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t10of12   align=  center   style=  Margin:0 auto;border-collapse:collapse;max-width:560px;width:100%  >
                    <tbody>
                      <tr>
                        <td style=  direction:ltr;text-align:left;padding-left:0;padding-right:0  >
                          <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                            <tbody>


  
  <tr>
    <td style=  direction:ltr;text-align:left;color:#000000;font-family:   Uber Move   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:24px;font-weight:500;line-height:30px;padding-bottom:7px;padding-left:12px;padding-right:12px;padding-top:7px  >
      Pick your favourite and enjoy.
    </td>
  </tr>

  <tr>
    <td style=  direction:ltr;text-align:left  >
    

        <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t5of12   align=  left   style=  border-collapse:collapse;max-width:374px;width:100%  >
          <tbody>
            <tr>
            
              <td width=  50%   style=  direction:ltr;text-align:left;padding-left:0;padding-right:0   valign=  top  >
                <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
                  <tbody>
                    <tr>
                      <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                        <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                          <tbody>
                            
                            
                            <tr>
                <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  Asiri Hotel  >
                  
                
                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Dfacd76f7-23fc-5d13-93a3-078679a469a7&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fasiri-hotel-kaduwela%2F-s129yP8XROToweGeaRppw&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D1   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Dfacd76f7-23fc-5d13-93a3-078679a469a7%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fasiri-hotel-kaduwela%252F-s129yP8XROToweGeaRppw%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D1&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw2_VLZgtf5u6K8uocrrs1gb  >
                <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
                <tbody>
                 <tr>
                 
                  
                  </tr><tr>
                   <td align=  right   valign=  bottom   style=  vertical-align:bottom;padding:4px 4px 4px 4px  >
                    <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                     <tbody>
                      <tr>
                       <td style=  color:#000000;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:300;line-height:10px;background-color:#e0e0e0;padding:4px 4px 4px 4px;border-radius:10px 10px 10px 10px  >
                       4.7
                       </td>
                      </tr>
                    </tbody></table>
                    </td>
                  </tr>
                  
                </tbody>
                </table>
                </a>
                    
                  
                </td>
                </tr>
                            
                            <tr>
                              <td style=  direction:ltr;text-align:left;padding-bottom:4px  >
                                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Dfacd76f7-23fc-5d13-93a3-078679a469a7&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fasiri-hotel-kaduwela%2F-s129yP8XROToweGeaRppw&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D1   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Dfacd76f7-23fc-5d13-93a3-078679a469a7%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fasiri-hotel-kaduwela%252F-s129yP8XROToweGeaRppw%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D1&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw1KDBq7-1rk71ZgyOlaT_Jx  >
                                  <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                   Asiri Hotel
                                  </span>
                                  <br>
                                  <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                                    $ • Sri Lankan
                                  </span>
                                  <br>
                                  <span style=  color:#036134;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    Order now →
                                  </span>
                                </a>
                              </td>
                            </tr>
                          
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>

              <td width=  50%   style=  direction:ltr;text-align:left;padding-left:0;padding-right:0   valign=  top  >
                <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
                  <tbody>
                    <tr>
                      <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                        <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                          <tbody>
                            
                            <tr>
                <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  KFC  >
                  
                
                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D35aa78eb-7426-41c5-8d8a-9ae651b21705&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fkfc-malabe%2FNap463QmQcWNiprmUbIXBQ&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D1   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D35aa78eb-7426-41c5-8d8a-9ae651b21705%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fkfc-malabe%252FNap463QmQcWNiprmUbIXBQ%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D1&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw2Ukw1RpV9UhfhiFFbEsGhR  >
                <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
                <tbody>
                 
                  
                  <tr>
                   <td align=  right   valign=  bottom   style=  vertical-align:bottom;padding:4px 4px 4px 4px  >
                    <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=     style=  table-layout:fixed;max-width:80%  >
                     <tbody>
                      <tr>
                       <td style=  color:#000000;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:8px;font-weight:300;line-height:10px;background-color:#e0e0e0;padding:4px 4px 4px 4px;border-radius:10px 10px 10px 10px  >
                       4.5
                       </td>
                      </tr>
                    </tbody></table>
                    </td>
                  </tr>
                  
                </tbody>
                </table>
                </a>
                    
                  
                </td>
                </tr>
                            <tr>
                              <td style=  direction:ltr;text-align:left;padding-bottom:4px  >
                                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D35aa78eb-7426-41c5-8d8a-9ae651b21705&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fkfc-malabe%2FNap463QmQcWNiprmUbIXBQ&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D2%26ds_sp%3D1   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D35aa78eb-7426-41c5-8d8a-9ae651b21705%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fkfc-malabe%252FNap463QmQcWNiprmUbIXBQ%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D2%2526ds_sp%253D1&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw04_QJ1I4N4bCoBuiZnELDU  >
                                  <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    KFC
                                  </span>
                                  <br>
                                  <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                                    $$ • American • Burgers
                                  </span>
                                  <br>
                                  <span style=  color:#036134;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    Order now →
                                  </span>
                                </a>
                              </td>
                            </tr>
                            
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>

            </tr>
          </tbody>
        </table>

"""

# Extract URLs from the input paragraph using urllib.parse
extracted_urls = extract_urls(paragraph_with_urls)

# Print extracted URLs
print("Extracted URLs:")
for url in extracted_urls:
    print(url)

for url in extracted_urls:
    try:
        # Call request.py script with the extracted URL as a command-line argument
        result = subprocess.run(["python", "../request.py", "-u", url], capture_output=True, text=True)
        output = result.stdout.strip()  # Get the output from the subprocess
        print(f"\nPhishing probability for {url}: {output}\n\n")
    except Exception as e:
        print(f"Error processing URL {url}: {e}")