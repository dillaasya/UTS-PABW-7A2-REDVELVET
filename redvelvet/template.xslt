<xsl:stylesheet version="1.0"
     xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
         <div class="toc-root">
             <ul>
                 <xsl:apply-templates/>
             </ul>
         </div>
     </xsl:template>
    <xsl:template match="row">
         <li>
          <div class="toc-row">
              <table border="1">
              <tbody>
              <tr><xsl:apply-templates select="row"/>
                <td  width="30px"><xsl:apply-templates select="Id"/></td>
                <td  width="80px"><xsl:apply-templates select="Name"/></td>
                <td  width="80px"><xsl:apply-templates select="Price"/></td>
              </tr>
              </tbody>
              </table>
          </div>
         </li>
     </xsl:template>
 </xsl:stylesheet>