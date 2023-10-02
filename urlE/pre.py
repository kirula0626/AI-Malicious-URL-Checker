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
 
<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border:none;border-collapse:collapse;border-spacing:0;width:100%  >
  <tbody>
  <tr>
    <td align=  left   style=  direction:ltr;text-align:left;padding:10px 14px 10px 14px;padding-left:0;background-color:#ffffff  >

      <table border=  0   cellpadding=  0   cellspacing=  0   style=  border:none;border-collapse:collapse;border-spacing:0;width:100%  >
      <tbody>
        <tr>
        <td width=  14   style=  direction:ltr;text-align:left;padding-left:0;padding-right:0  ><img width=  14   height=  54   style=  clear:both;display:block;max-width:100%;outline:none;text-decoration:none   border=  0   alt=    >
        </td>

        <td style=  direction:ltr;text-align:left;font-size:0  >
        

        <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t1of12   style=  border:none;border-collapse:collapse;border-spacing:0;max-width:56px;width:100%;display:inline-block;vertical-align:middle  >
        <tbody>
          <tr>
          <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
            <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border:none;border-collapse:collapse;border-spacing:0;table-layout:fixed;width:100%  >
              <tbody>
                <tr>
                <td height=  2   style=  direction:ltr;text-align:left;font-size:0;line-height:1px  >
                &nbsp;
                </td>
              </tr>
              </tbody>
            </table>
          </td>
          </tr>
        </tbody>
        </table>



      

  <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t11of12   style=  border:none;border-collapse:collapse;border-spacing:0;max-width:616px;width:100%;display:inline-block;vertical-align:middle  >
    <tbody>
      <tr>
      <td style=  direction:ltr;text-align:left;padding-left:0;padding-right:0  >
      <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border:none;border-collapse:collapse;border-spacing:0;table-layout:fixed;width:100%  >
        <tbody>
          <tr>
            <td style=  direction:ltr;text-align:left;font-size:0  >
              

              <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t4of12   style=  border:none;border-collapse:collapse;border-spacing:0;display:inline-block;max-width:408px;vertical-align:middle;width:100%  >
                <tbody>
                  <tr>
                  <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                      <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border:none;border-collapse:collapse;border-spacing:0;table-layout:fixed;width:100%  >
                        <tbody>



                    

                        
                        <tr>
                        <td style=  direction:ltr;text-align:left;font-size:0  >

                          <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border:none;border-collapse:collapse;border-spacing:0;table-layout:fixed;width:100%  >
                            <tbody>
                              <tr>
                              <td style=  direction:ltr;text-align:left;color:#000000;font-family:   UberMoveText-Regular   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:0;line-height:26px;padding-bottom:0px;padding-top:0px  >

                                
                                 <a href=  http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3PTWD1XrrsuiXVNpxIMMrRkpnboC2Fsdovf95YuNHm-5/400/qipDk_wIQiieKe1Ha64Jnw/h0/M1PI63CYAmijqu04jPd1vmpCXIEY7jcj8HUQVGBqDqs   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3PTWD1XrrsuiXVNpxIMMrRkpnboC2Fsdovf95YuNHm-5/400/qipDk_wIQiieKe1Ha64Jnw/h0/M1PI63CYAmijqu04jPd1vmpCXIEY7jcj8HUQVGBqDqs&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw2T0H6sfuytNM1Ohtah_sxw  >
                                <img width=  147   height=  43   style=  clear:both;display:block;max-width:100%;outline:none;text-decoration:none   alt=  Uber Eats  >
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
</tbody></table>




                             



</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>
</td>
</tr>












</tbody></table>





















  
    
    
    
    
  






<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
<tbody>
<tr>
<td style=  padding-bottom:0px  >
<table border=  0   cellpadding=  0   cellspacing=  0   style=  width:100%  >

<tbody><tr>
 <td width=  100%   height=     valign=  middle   style=  background-size:cover;background-image:url(      );background-size:100%;background-repeat:no-repeat;background-position:100% 100%   align=  left   alt=  Big savings for more than one craving   bgcolor=  0F462D  >
 	
 
<a href=  http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3LpA2wOFVQaap3oh57xd8tE/400/qipDk_wIQiieKe1Ha64Jnw/h1/ESW1t9eNxGB0vzwBWQMmUVUVQp8LDUKABbKOZZUb9ac   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3LpA2wOFVQaap3oh57xd8tE/400/qipDk_wIQiieKe1Ha64Jnw/h1/ESW1t9eNxGB0vzwBWQMmUVUVQp8LDUKABbKOZZUb9ac&amp;source=gmail&amp;ust=1696108604056000&amp;usg=AOvVaw2F8b7H0DrOHDvjTcoqn7JM  >
 <table border=  0   cellpadding=  0   cellspacing=  0   valign=  middle   align=  center   style=  border:none;border-collapse:collapse;border-spacing:0;max-width:588px;width:100%  >
   <tbody>
	<tr>
		<td>
		  <img width=  88%   height=     style=  display:block;width:88%;height:auto;outline:none;text-decoration:none   border=  0   alt=    >
		</td>
	</tr>
	<tr>
	  <td style=  padding:0 26px 0 26px  >
		 <table border=  0   cellpadding=  0   cellspacing=  0   width=  auto   align=  left   style=  table-layout:fixed;max-width:60%  >
			<tbody>
			 <tr>
				<td>
				<h2 class=  m_5925240524307192452h2   style=  Margin:0;padding:10px 0 10px 0;font-family:   Uber Move   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:28px;line-height:34px;font-weight:500;color:#ffffff  >
				Big savings for more than one craving
				</h2>
				</td>
			 </tr>
		   </tbody></table>
		 </td>
	 </tr>
	 <tr>
		<td>
		  <img width=  88%   height=     style=  display:block;width:88%;height:auto;outline:none;text-decoration:none   border=  0   alt=    >
		</td>
	 </tr>
 </tbody>
 </table>
</a>
		 
	 
 </td>
 </tr>

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

         

         
         <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t1of12 m_5925240524307192452thirdwheel   align=  left   style=  border-collapse:collapse;max-width:186px;width:100%  >
            <tbody>
              <tr>
                <td style=  direction:ltr;text-align:left;padding-left:12px;padding-right:12px  >
                  <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                    <tbody>
                      
                      <tr>
            <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  Pizza Hut  >
              
            
            <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Ddc54ea24-08a9-5450-9eac-f2fed6d8bacd&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fpizza-hut-kothalawala-malabe%2F3FTqJAipVFCerPL-1ti6zQ&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D1   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Ddc54ea24-08a9-5450-9eac-f2fed6d8bacd%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fpizza-hut-kothalawala-malabe%252F3FTqJAipVFCerPL-1ti6zQ%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D1&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw01WFwZSCxZ6QhAjxL4-ENx  >
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
                          <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Ddc54ea24-08a9-5450-9eac-f2fed6d8bacd&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fpizza-hut-kothalawala-malabe%2F3FTqJAipVFCerPL-1ti6zQ&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D3%26ds_sp%3D1   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Ddc54ea24-08a9-5450-9eac-f2fed6d8bacd%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fpizza-hut-kothalawala-malabe%252F3FTqJAipVFCerPL-1ti6zQ%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D3%2526ds_sp%253D1&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw2NqYzjebEAoWcoC4eodFRT  >
                            <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                              Pizza Hut
                            </span> <br>
                            <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                              $ • American • Italian
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
      Discover foodie recommendations you can’t resist
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
                <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  Elite Family Restaurant  >
                  
                
                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D8cbb447a-1d21-432f-8d09-551bd7236d4c&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Felite-family-restaurant-battaramulla%2FjLtEeh0hQy-NCVUb1yNtTA&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D2   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D8cbb447a-1d21-432f-8d09-551bd7236d4c%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Felite-family-restaurant-battaramulla%252FjLtEeh0hQy-NCVUb1yNtTA%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D2&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw0PWFmL5vG5OKX6RBGgLWjo  >
                <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
                <tbody>
                 <tr>
                 
                  
                  </tr><tr>
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
                                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D8cbb447a-1d21-432f-8d09-551bd7236d4c&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Felite-family-restaurant-battaramulla%2FjLtEeh0hQy-NCVUb1yNtTA&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D2   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D8cbb447a-1d21-432f-8d09-551bd7236d4c%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Felite-family-restaurant-battaramulla%252FjLtEeh0hQy-NCVUb1yNtTA%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D2&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw0PWFmL5vG5OKX6RBGgLWjo  >
                                  <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                   Elite Family Restaurant
                                  </span>
                                  <br>
                                  <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                                    $$ • Asian • Biryani
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
                <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  P&amp;S  >
                  
                
                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D12e58b8a-843b-4d67-a384-bfb0615a6756&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fp%2526s-perera-and-sons-athurugiriya%2FEuWLioQ7TWejhL-wYVpnVg&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D2   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D12e58b8a-843b-4d67-a384-bfb0615a6756%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fp%252526s-perera-and-sons-athurugiriya%252FEuWLioQ7TWejhL-wYVpnVg%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D2&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw3WhP7-vdud5iCI1YAGSJ3_  >
                <table border=  0   cellpadding=  0   cellspacing=  0   valign=  bottom   align=     style=  border:none;border-collapse:collapse;border-spacing:0;max-width:163px;width:100%  >
                <tbody>
                 
                  
                  <tr>
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
                                <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3D12e58b8a-843b-4d67-a384-bfb0615a6756&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Fp%2526s-perera-and-sons-athurugiriya%2FEuWLioQ7TWejhL-wYVpnVg&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D2%26ds_sp%3D2   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253D12e58b8a-843b-4d67-a384-bfb0615a6756%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Fp%252526s-perera-and-sons-athurugiriya%252FEuWLioQ7TWejhL-wYVpnVg%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D2%2526ds_sp%253D2&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw21VRRrgQiVhE6u0J1KUObP  >
                                  <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                                    P&amp;S
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
            <td bgcolor=  #f1f1f1   height=  106   valign=  bottom   style=  background-size:cover;background-image:url(      );background-position:50% 50%   align=     alt=  Indian Affair  >
              
            
            <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Dbaf88cf1-3f6c-5a4b-b16b-9cf2028dae8e&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Findian-affair-thalawathugoda%2FuviM8T9sWkuxa5zyAo2ujg&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D1%26ds_sp%3D2   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Dbaf88cf1-3f6c-5a4b-b16b-9cf2028dae8e%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Findian-affair-thalawathugoda%252FuviM8T9sWkuxa5zyAo2ujg%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D1%2526ds_sp%253D2&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw3khCTDfSTYMdroQq8zRX0x  >
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
                          <a href=  https://ubereats.app.link/cwmLFZfMz5?%243p=a_custom_354088&amp;%24deeplink_path=ubereats%3A%2F%2Fstore%2Fbrowse%3FstoreUUID%3Dbaf88cf1-3f6c-5a4b-b16b-9cf2028dae8e&amp;%24desktop_url=https%3A%2F%2Fwww.ubereats.com%2Fstore%2Findian-affair-thalawathugoda%2FuviM8T9sWkuxa5zyAo2ujg&amp;~customer_keyword=27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee&amp;custom_fields=ds_mp%3D3%26ds_sp%3D2   style=  text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=https://ubereats.app.link/cwmLFZfMz5?%25243p%3Da_custom_354088%26%2524deeplink_path%3Dubereats%253A%252F%252Fstore%252Fbrowse%253FstoreUUID%253Dbaf88cf1-3f6c-5a4b-b16b-9cf2028dae8e%26%2524desktop_url%3Dhttps%253A%252F%252Fwww.ubereats.com%252Fstore%252Findian-affair-thalawathugoda%252FuviM8T9sWkuxa5zyAo2ujg%26~customer_keyword%3D27d8ef65-d1dd-3568-bfbe-d27f4cd3e7ee%26custom_fields%3Dds_mp%253D3%2526ds_sp%253D2&amp;source=gmail&amp;ust=1696108604057000&amp;usg=AOvVaw2j5CthodZm5fQrm3-Siluk  >
                            <span style=  color:#000000;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:16px;font-weight:500;line-height:22px;padding-bottom:7px;padding-top:7px  >
                              Indian Affair
                            </span> <br>
                            <span style=  color:#909090;font-family:   Uber Move Text   ,   Helvetica Neue   ,Helvetica,Arial,sans-serif;font-size:14px;font-weight:normal;line-height:22px;padding-bottom:7px;padding-top:0  >
                              $ • Indian • Biryani
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



</tbody>
</table>














        
  
  


  
    
    
  




  
        
  

  
        
  



<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
   <tbody>

      <tr>
      <td align=  left   style=  direction:ltr;text-align:left;background-color:#ffffff;padding-left:14px;padding-right:14px;padding-top:15px;padding-bottom:15px  >
         <table border=  0   cellpadding=  0   cellspacing=  0   style=  border-collapse:collapse;width:100%  >
            <tbody><tr>
               <td style=  direction:ltr;text-align:left  >

         <table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t10of12   align=  center   style=  Margin:0 auto;border-collapse:collapse;max-width:560px;width:100%  >
            <tbody><tr>
               <td style=  direction:ltr;text-align:left;padding-bottom:0px;padding-left:12px;padding-right:12px;padding-top:0px  >
                  <table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  border-collapse:collapse;table-layout:fixed;width:100%  >
                     <tbody><tr>
                        <td style=  direction:ltr;text-align:left;color:#000000;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:12px;font-weight:normal;line-height:18px;padding-bottom:7px;padding-top:7px  ><div>The following terms apply based on the offer type. Offer availability may change without notice based on user, merchant location and time of order. Except for the LKR&nbsp;0 delivery fee, offers do not apply to delivery and other fees on eligible order(s). Offers for buy one get one / free item(s) are applied as a promotion on the selected menu item price only, and delivery and other fees will still apply on the full order total. Minimum order requirement applies if specified and does not include any delivery or other fees applied to the order. Any remaining offer value is forfeited if order value is below the minimum amount specified. LKR&nbsp;0 delivery fee will be applied as a promotion. Cannot be combined. Offer may be limited to a single order only. All offers are non-transferable. See app for current available offers and terms.</div>
</td>
                     </tr>
                  </tbody></table>
               </td>
            </tr>
         </tbody></table>
         
               </td>
            </tr>
         </tbody></table>
      </td>
   </tr>
 
</tbody></table>

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

</tbody>
</table>
 
<table width=  100%   border=  0   cellpadding=  0   cellspacing=  0   style=  background-color:#000000;width:100%  >
<tbody><tr>
<td align=  left   style=  direction:ltr;text-align:left  >
<table border=  0   cellpadding=  0   cellspacing=  0   style=  width:100%  >






<tbody><tr>
<td style=  direction:ltr;text-align:left;padding:30px 14px 30px 14px  >

<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t10of12   align=  center   style=  Margin:0 auto;max-width:560px;width:100%  >
<tbody><tr>
<td>
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  direction:rtl;table-layout:fixed;width:100%  >
<tbody><tr>
<td style=  font-size:0;text-align:left  >
<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t6of12   style=  direction:ltr;display:inline-block;max-width:560px;vertical-align:top;width:100%  >
<tbody><tr>
<td>
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  table-layout:fixed;width:100%  >
<tbody><tr>
<td>

<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t3of12   align=  left   style=  max-width:168px;width:100%  >
<tbody><tr>
<td style=  direction:ltr;text-align:left;padding:0 12px  >
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  table-layout:fixed;width:100%  >

<tbody><tr>
<td style=  color:rgb(0,0,0);font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:12px;line-height:18px;padding:3px 0px;direction:ltr;text-align:left  >


<a href=  http://email.uber.com/ss/c/sucETp6dPi8qQ9tD78Dzi8uiN7eHjEwKCG1FmrlEVBWd-jZxgvPan3dEIJE2EBQ1/400/qipDk_wIQiieKe1Ha64Jnw/h2/IQWcIvc4fbRhIZhEKsqGt64b2yYgOEwLh16dPAHdIAE   style=  color:rgb(255,255,255);text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/sucETp6dPi8qQ9tD78Dzi8uiN7eHjEwKCG1FmrlEVBWd-jZxgvPan3dEIJE2EBQ1/400/qipDk_wIQiieKe1Ha64Jnw/h2/IQWcIvc4fbRhIZhEKsqGt64b2yYgOEwLh16dPAHdIAE&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw0csrao7SYHBtAUENLtfa1S  >Help Center</a>


</td>
</tr>




<tr>
<td style=  color:rgb(0,0,0);font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:12px;line-height:18px;padding:3px 0px;direction:ltr;text-align:left  >

<a href=  http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3E0oymevE-d6JU08iC1ny_13PBgvuU8lAW6SohDZm9H-rbjMUH-OWPWGmNk1GYPPPZMV8kmCXQRwfzx-XTzCptjh-Dc0SL-onyxtxAEvcxiQBN-iAxvQVwuddxDoJIUrtiInrWSQfk-x6L7nWneiHm_auJBfyCAEkRqRQq0k9omuMToVfbtMLO9SMxfPQG5gz1UCiru9-NJOQnbKXWHUqyc0zkb7deiMXtTQKlKxn0HgOb2ELSOIIpqWdL0H9c1PvbVOl5jA8OjsxDEYhxG7I-R89RmR-H-L32BeOLukEZ_f_7X2d7O5v8D1nYXUO-t9ABWxeJse7wO-AeIBjoKWkzRpOXAgX8hxPYro8371rjZrXIuV3jTrB5sT67Zf35QZVIifOREaEwW4mVjdWhwzGtDE8uMljxeQtmbf5FfCjwFj_wijXBnBaCM-qLIza3xWc7fDsGxNHLLTtWec7nOOtxg2l05GiVbMkzUg_sI8zKYCUO7CZbjrDGs8fhTl7CJlG4mypcDsBlXVojVkponV-iqyLBDQJokwMxCaXTLkiGcZZRHZ4pMIopCVPVN0wJ0KcDiBfaNm50a6UKSKMBO525W064Rv4D60XyBUqKa5prCYBo1nT_cWQmZz6rRyB-bEQVLJjLUeBdpwqA3NdswZfYUmJEBneXt0g60Kyev_XU-ZHZQ31vtP9EJ-r7mIaZ8w3KTncQgHE2xmvumANKR-dBqY3oiuK4uP_HdubDaOcPJVDhb0gGgz2Bsc9brhpeHcK8PuwUs9OJV4bHKW7cCtTNL2xqDzl9m1s1o27wVWyR_ARv_M_-XFZjTK2_Rn665xyDEDQokS_nCb4I0EZB4u6-tDGKlRm-HJFLdhRcoaK2XBus3C6Gev3Zzgsz_wA-7OXNtFQUhjw2Tbyw0OLt6Ozb0OAb-Lstjb7siFp5L8xYFUF5qkBov3TyYY8fLJZI4ypVtxlVZsFZpzqXTxSRg2UUMQ5lsuS9oR__A1Fu2BK5aAJpx_nrxKDVcsyolPwDKurroXDKbl0KjQsSiMP6jDeXrA50BIiYbmFv9-iDy8x3iQMFM1SPrA4PiVppY1CMKa_g/400/qipDk_wIQiieKe1Ha64Jnw/h3/Sc8NzXG7CgbtMuLzOQd2Mm3VJpvizptMlKBFYdrvfiI   style=  text-decoration:none;color:#ffffff   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3E0oymevE-d6JU08iC1ny_13PBgvuU8lAW6SohDZm9H-rbjMUH-OWPWGmNk1GYPPPZMV8kmCXQRwfzx-XTzCptjh-Dc0SL-onyxtxAEvcxiQBN-iAxvQVwuddxDoJIUrtiInrWSQfk-x6L7nWneiHm_auJBfyCAEkRqRQq0k9omuMToVfbtMLO9SMxfPQG5gz1UCiru9-NJOQnbKXWHUqyc0zkb7deiMXtTQKlKxn0HgOb2ELSOIIpqWdL0H9c1PvbVOl5jA8OjsxDEYhxG7I-R89RmR-H-L32BeOLukEZ_f_7X2d7O5v8D1nYXUO-t9ABWxeJse7wO-AeIBjoKWkzRpOXAgX8hxPYro8371rjZrXIuV3jTrB5sT67Zf35QZVIifOREaEwW4mVjdWhwzGtDE8uMljxeQtmbf5FfCjwFj_wijXBnBaCM-qLIza3xWc7fDsGxNHLLTtWec7nOOtxg2l05GiVbMkzUg_sI8zKYCUO7CZbjrDGs8fhTl7CJlG4mypcDsBlXVojVkponV-iqyLBDQJokwMxCaXTLkiGcZZRHZ4pMIopCVPVN0wJ0KcDiBfaNm50a6UKSKMBO525W064Rv4D60XyBUqKa5prCYBo1nT_cWQmZz6rRyB-bEQVLJjLUeBdpwqA3NdswZfYUmJEBneXt0g60Kyev_XU-ZHZQ31vtP9EJ-r7mIaZ8w3KTncQgHE2xmvumANKR-dBqY3oiuK4uP_HdubDaOcPJVDhb0gGgz2Bsc9brhpeHcK8PuwUs9OJV4bHKW7cCtTNL2xqDzl9m1s1o27wVWyR_ARv_M_-XFZjTK2_Rn665xyDEDQokS_nCb4I0EZB4u6-tDGKlRm-HJFLdhRcoaK2XBus3C6Gev3Zzgsz_wA-7OXNtFQUhjw2Tbyw0OLt6Ozb0OAb-Lstjb7siFp5L8xYFUF5qkBov3TyYY8fLJZI4ypVtxlVZsFZpzqXTxSRg2UUMQ5lsuS9oR__A1Fu2BK5aAJpx_nrxKDVcsyolPwDKurroXDKbl0KjQsSiMP6jDeXrA50BIiYbmFv9-iDy8x3iQMFM1SPrA4PiVppY1CMKa_g/400/qipDk_wIQiieKe1Ha64Jnw/h3/Sc8NzXG7CgbtMuLzOQd2Mm3VJpvizptMlKBFYdrvfiI&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw306ePlu3xwTidVUvu52Sbi  >Unsubscribe</a>

</td>
</tr>


<tr>
<td style=  color:rgb(0,0,0);font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:12px;line-height:18px;padding:3px 0px;direction:ltr;text-align:left  >


<a href=  http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3NZSO_R7xQ_qQdUWaodCICLyoyrUaikfMh8St3tq-Zk2/400/qipDk_wIQiieKe1Ha64Jnw/h4/7lo8lTQshkJtIKFsnhQTIeNSrTwT0E08gfm2oozvSiU   style=  color:rgb(255,255,255);text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3NZSO_R7xQ_qQdUWaodCICLyoyrUaikfMh8St3tq-Zk2/400/qipDk_wIQiieKe1Ha64Jnw/h4/7lo8lTQshkJtIKFsnhQTIeNSrTwT0E08gfm2oozvSiU&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw0-qwza4-Q_ES_2jqw5zZqK  >Terms</a>


</td>
</tr>




</tbody></table>
</td>
</tr>
</tbody></table>

<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t3of12   align=  left   style=  max-width:300px;width:100%  >
<tbody><tr>
<td style=  direction:ltr;text-align:left;padding:0 12px  >
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  table-layout:fixed;width:100%  >
<tbody><tr>
<td style=  color:rgb(0,0,0);font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:12px;line-height:18px;padding:3px 0px;direction:ltr;text-align:left  >


<a href=  http://email.uber.com/ss/c/NtS8hnLZtsEC-6Wun150xZlT51rk8lUEc5R5UIv5tgmIA2NiysiHgAxTpfawkyxm/400/qipDk_wIQiieKe1Ha64Jnw/h5/5_Eqc8xMq-N-_WLPVUbE0miIUbCEShEyFv_lxImw6XE   style=  color:rgb(255,255,255);text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/NtS8hnLZtsEC-6Wun150xZlT51rk8lUEc5R5UIv5tgmIA2NiysiHgAxTpfawkyxm/400/qipDk_wIQiieKe1Ha64Jnw/h5/5_Eqc8xMq-N-_WLPVUbE0miIUbCEShEyFv_lxImw6XE&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw3-3qZVnWbZWbHKFoZ-5ygz  >Privacy</a> 


</td>
</tr>



<tr>
<td style=  color:rgb(0,0,0);font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:12px;line-height:18px;padding:3px 0px;direction:ltr;text-align:left  >
<a href=  http://email.uber.com/ss/c/tJraAOLos0F6jr36KJg0DBny2x7ghDV78i_L0vstwfUSehGYiYdyg576x21xVxNx/400/qipDk_wIQiieKe1Ha64Jnw/h6/jInLx7k6Qr8rG6u-meNN-JX7JvhmZqwdybucD_DQJC4   style=  color:rgb(255,255,255);text-decoration:none   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/tJraAOLos0F6jr36KJg0DBny2x7ghDV78i_L0vstwfUSehGYiYdyg576x21xVxNx/400/qipDk_wIQiieKe1Ha64Jnw/h6/jInLx7k6Qr8rG6u-meNN-JX7JvhmZqwdybucD_DQJC4&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw2UyGWxyRhfQU2Gk_nxUW-8  >Email Preferences</a>
</td>
</tr>


</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>


<tr>
<td style=  direction:ltr;text-align:left;padding:0px 14px 30px 14px  >

<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t10of12   align=  center   style=  Margin:0 auto;max-width:560px;width:100%  >
<tbody><tr>
<td>
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  direction:rtl;table-layout:fixed;width:100%  >
<tbody><tr>
<td style=  font-size:0;text-align:left  >

<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t4of12   style=  direction:ltr;display:inline-block;max-width:224px;vertical-align:top;width:100%  >
<tbody><tr>
<td style=  direction:ltr;text-align:left;padding:0 12px  >
<table border=  0   cellpadding=  0   cellspacing=  0   align=  left   style=  table-layout:fixed  >
<tbody><tr>
<td style=  padding-bottom:12px;direction:ltr;text-align:left  >


<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  table-layout:fixed;width:130px  >
<tbody><tr>
<td width=  43   align=  center   style=  direction:ltr;text-align:left  >
<a href=  http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3HRFSTRAozALynJoj2hCBXy-A7AjPrAZy-BKqssmVw39/400/qipDk_wIQiieKe1Ha64Jnw/h7/SwEXgA2haP1zEvIHIIzISy079I888UzH_eNMFtgJqnE   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3HRFSTRAozALynJoj2hCBXy-A7AjPrAZy-BKqssmVw39/400/qipDk_wIQiieKe1Ha64Jnw/h7/SwEXgA2haP1zEvIHIIzISy079I888UzH_eNMFtgJqnE&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw32Pp5CaiqjeU3VQV0SAqYu  > <img width=  13   height=     border=  0   style=  display:block;height:auto;max-height:17px;max-width:13px;width:100%  >
</a>
</td>
<td width=  43   align=  center   style=  direction:ltr;text-align:left  >
<a href=  http://email.uber.com/ss/c/LbqnkeGlYGM_2j-spoQ5q8jWfHMdofuc9WtgWFVNP_g/400/qipDk_wIQiieKe1Ha64Jnw/h8/YxZDKl2FuCw_qrWEuVhmWAtUGWNQap47oAttzN36WAI   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/LbqnkeGlYGM_2j-spoQ5q8jWfHMdofuc9WtgWFVNP_g/400/qipDk_wIQiieKe1Ha64Jnw/h8/YxZDKl2FuCw_qrWEuVhmWAtUGWNQap47oAttzN36WAI&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw1-DfKurQsD3Uxkw0VGK7LU  > <img width=  19   height=     border=  0   style=  display:block;height:auto;max-height:17px;max-width:19px;width:100%  >
</a>
</td>
<td width=  43   align=  center   style=  direction:ltr;text-align:left  >
<a href=  http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3J9tUWmut990WG8GGZmBFPsvp6GdO90yBl5qfYd5L0Ap/400/qipDk_wIQiieKe1Ha64Jnw/h9/_FTSgtmeAk-UPMPY94uvrf4ki2bNgBU3vc3OefUNQOc   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/lKT8ccCkHTtPXRlUdr2M3J9tUWmut990WG8GGZmBFPsvp6GdO90yBl5qfYd5L0Ap/400/qipDk_wIQiieKe1Ha64Jnw/h9/_FTSgtmeAk-UPMPY94uvrf4ki2bNgBU3vc3OefUNQOc&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw2inSuouUyUnrPHViSsf6dL  > <img width=  16   height=     border=  0   style=  display:block;height:auto;max-height:17px;max-width:16px;width:100%  >
</a>
</td>
</tr>
</tbody></table>

 
</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

<table border=  0   cellpadding=  0   cellspacing=  0   class=  m_5925240524307192452t6of12   style=  direction:ltr;display:inline-block;max-width:336px;vertical-align:top;width:100%  >
<tbody><tr>
<td style=  direction:ltr;text-align:left;padding:0 12px  >
<table border=  0   cellpadding=  0   cellspacing=  0   width=  100%   align=  left   style=  table-layout:fixed;width:100%  >
<tbody><tr>
<td style=  direction:ltr;text-align:left;color:#e5e5e5;font-family:   Uber Move Text   ,   HelveticaNeue   ,Helvetica,Arial,sans-serif;font-size:10px;line-height:18px  >









Uber B.V.


<br>




Burgerweeshuispad 301,<br>
1076 HR Amsterdam, Netherlands


<br>

<a href=  http://email.uber.com/ss/c/wzdQCNDdlxxHNAIyua_dK1CVDlEfPJHPAJ1wpnyR5Aw/400/qipDk_wIQiieKe1Ha64Jnw/h10/qrJVxzpS43Yc8nSJp-6OtwuDHsa4J26LRchWQOLfjHA   style=  text-decoration:none;color:#e5e5e5   target=  _blank   data-saferedirecturl=  https://www.google.com/url?q=http://email.uber.com/ss/c/wzdQCNDdlxxHNAIyua_dK1CVDlEfPJHPAJ1wpnyR5Aw/400/qipDk_wIQiieKe1Ha64Jnw/h10/qrJVxzpS43Yc8nSJp-6OtwuDHsa4J26LRchWQOLfjHA&amp;source=gmail&amp;ust=1696108604058000&amp;usg=AOvVaw0xkutQnjT_b5MOyM25So6x  >Uber.com</a>

</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>


</tbody></table>
</td>
</tr>
</tbody></table>

</td>
</tr>
</tbody>
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