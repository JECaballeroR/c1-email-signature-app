import streamlit as st
import base64

# Page config
st.set_page_config(page_title="C1 Email Signature Generator", layout="wide")

# Sidebar inputs
st.sidebar.title("Signature Configuration")
first_name = st.sidebar.text_input("First Name", "Jorge")
last_name = st.sidebar.text_input("Last Name", "Caballero")
position = st.sidebar.text_input("Position", "Web Developer")
meeting_link = st.sidebar.text_input("Meeting Link (optional)", "https://correlation-one.com/meetings/jorge-esteban-caballero")
cta_text = st.sidebar.text_input("CTA Text", "Let's chat")
cta_followup = st.sidebar.text_input("CTA Follow-up Text", "if you’re curious about data literacy upskilling for company.")

# Conditionally include PS block
ps_html = f"""
<tr>
  <td style=\"padding-top: 10px;\">
    <table width=\"100%\" style=\"background-color: #ffffff; border-radius: 8px;\">
      <tr>
        <td style=\"padding: 8px 8px; font-size: 13px; color: #575c64; font-family: Arial, sans-serif;\">
          P.S. <a href=\"{meeting_link}\" style=\"color: #0066cc; font-weight: 600; text-decoration: none;\">{cta_text}</a> {cta_followup}
        </td>
      </tr>
    </table>
  </td>
</tr>
""" if meeting_link.strip() else ""

# Email signature HTML
html_signature = f"""
<div style=\"max-width: 513px;\">
  <table cellspacing=\"0\" style=\"border: none; font-size: 100%; line-height: 13px; width: 100%; border-collapse: collapse; border-radius: 20px;\">
    <tbody>
      <tr>
        <td style=\"width: 100%; border-radius: 20px; padding: 0px;\">
          <table cellspacing=\"0\" style=\"background-color: #f6f7fc; padding: 24px; border-radius: 20px; width: 100%; border-collapse: separate;\">
            <tbody>
              <tr>
                <td style=\"padding: 0px;\">
                  <table width=\"100%\" cellspacing=\"0\" cellpadding=\"0\">
                    <tr>
                      <td style=\"width: 30%; background-color: #ffffff; border-top-left-radius: 8px; border-bottom-left-radius: 8px; vertical-align: middle; padding: 16px 24px; text-align: left;\">
                        <span style=\"font-weight: bold; font-size: 20px; color: #001730; font-family: Arial, Helvetica, sans-serif; line-height: 1.2; display: block;\">{first_name}</span>
                        <span style=\"font-weight: bold; font-size: 20px; color: #001730; font-family: Arial, Helvetica, sans-serif; line-height: 1.2; display: block;\">{last_name}</span>
                      </td>
                      <td style=\"background-color: #ffffff; border-top-right-radius: 8px; border-bottom-right-radius: 8px; padding: 12px 12px; width: 70%; vertical-align: middle;\">
                        <table cellspacing=\"0\" width=\"100%\">
                          <tbody>
                            <tr>
                              <td style=\"font-size: 13px; color: #001730; font-family: Arial, sans-serif; padding: 0px;\">{position}</td>
                            </tr>
                            <tr>
                              <td style=\"font-size: 13px; color: #575c64; font-family: Arial, sans-serif; padding: 2px 0px 0px;\">Correlation One</td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              {ps_html}
              <tr>
                <td style=\"text-align: center; padding: 16px 0;\">
                  <img src=\"https://www.correlation-one.com/hubfs/Group%202%20(1).png\" alt=\"Color bar\" style=\"max-width: 55%; height: auto; display: inline-block; margin-right:-228px\">
                </td>
              </tr>
              <tr>
                <td style=\"padding-top: 12px;\">
                  <table width=\"100%\" cellspacing=\"0\">
                    <tr>
                      <td style=\"padding: 0px;\" align=\"left\">
                        <a href=\"https://www.correlation-one.com/\" target=\"_blank\">
                          <img src=\"https://www.correlation-one.com/hubfs/C1%20Logo%20Dark%201.png\" width=\"130\" alt=\"Correlation One\" style=\"display: block;\">
                        </a>
                      </td>
                      <td style=\"padding: 0px;\" align=\"right\">
                        <table cellspacing=\"0\">
                          <tr>
                            <td><a href=\"https://web.facebook.com/correlationone/\" target=\"_blank\"><img src=\"https://www.correlation-one.com/hubfs/fb.png\" width=\"7\" alt=\"Facebook\" style=\"margin-left: 10px;\"></a></td>
                            <td><a href=\"https://www.linkedin.com/company/correlation-one/\" target=\"_blank\"><img src=\"https://www.correlation-one.com/hubfs/Lin.png\" width=\"17\" alt=\"LinkedIn\" style=\"margin-left: 10px;\"></a></td>
                            <td><a href=\"https://twitter.com/CorrelationOne\" target=\"_blank\"><img src=\"https://www.correlation-one.com/hubfs/X.png\" width=\"18\" alt=\"X\" style=\"margin-left: 10px;\"></a></td>
                            <td><a href=\"https://www.youtube.com/@correlationone\" target=\"_blank\"><img src=\"https://www.correlation-one.com/hubfs/YT.png\" width=\"22\" alt=\"YouTube\" style=\"margin-left: 10px;\"></a></td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</div>
"""

st.markdown("## 📥 Download Your C1 Email Signature")

# Optional: Allow user to download the HTML
html_download = f"<html><body>{html_signature}</body></html>"
html_bytes = html_download.encode("utf-8")
b64 = base64.b64encode(html_bytes).decode()
href = f'<a href="data:text/html;base64,{b64}" download="c1_signature.html">⬇️ Download HTML file</a>'
st.markdown(href, unsafe_allow_html=True)

with st.expander("📩 How to add this signature to Gmail"):
    st.markdown("""
1. **Download** the signature using the button above. This will save a `.html` file to your computer. You can download it as soon as you put the correct information in the sidebar.
2. **Open the downloaded file** in your web browser (double-click or right-click → “Open with” → your browser).
3. **Select the entire signature** by clicking and dragging, or pressing `Ctrl+A` (`Cmd+A` on Mac).
4. **Copy** the selection with `Ctrl+C` (`Cmd+C` on Mac).
5. Go to [**Gmail Settings**](https://mail.google.com/), click the ⚙️ gear icon, then **"See all settings"**.
6. In the **"General"** tab, scroll down to the **"Signature"** section.
7. Click **“Create new”**, name your signature, and **paste** the copied content into the editor using `Ctrl+V` (`Cmd+V` on Mac).
8. Optionally, set it as your default signature for new emails and replies.
9. Scroll down and click **“Save Changes.”**
    """)
