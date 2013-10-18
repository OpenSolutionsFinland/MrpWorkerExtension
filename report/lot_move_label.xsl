<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:fo="http://www.w3.org/1999/XSL/Format" xmlns:xs="http://www.w3.org/2001/XMLSchema" version="1.0">
	<xsl:variable name="initial_bottom_pos">-5</xsl:variable>
	<xsl:variable name="initial_left_pos">6</xsl:variable>
	<xsl:variable name="height_increment">5.8</xsl:variable>
	<xsl:variable name="width_increment">9</xsl:variable>
	<xsl:variable name="frame_height">15cm</xsl:variable>
	<xsl:variable name="frame_width">10cm</xsl:variable>
	<xsl:variable name="number_columns">3</xsl:variable>
	<xsl:variable name="max_frames">21</xsl:variable>
	

	<xsl:template match="/">
		<xsl:apply-templates select="lots"/>
		<xsl:variable name="dt" as="xs:dateTime" select="creationdate"/>
	</xsl:template>

	<xsl:template match="lots">
		<document>
			<template leftMargin="1cm" rightMargin="1cm" topMargin="1cm" bottomMargin="1cm" title="Address list" author="Generated by Open ERP">
				<pageTemplate id="all">
					<pageGraphics/>
					<xsl:apply-templates select="lot-line" mode="frames"/>
				</pageTemplate>
			</template>
			<stylesheet>
				<paraStyle name="nospace" fontName="Courier" fontSize="10" spaceBefore="0" spaceAfter="0" />
				<paraStyle name="small" fontName="Courier" fontSize="7" spaceBefore="0" spaceAfter="0"/>
				<paraStyle name="centered" fontName="Courier" fontSize="7" spaceBefore="0" spaceAfter="0" alignment="center"/>
				<paraStyle name="right" fontName="Courier" fontSize="7" spaceBefore="0" spaceAfter="0" alignment="right"/>
			</stylesheet>
			<story>
				<xsl:apply-templates select="lot-line" mode="story"/>
			</story>
		</document>
	</xsl:template>

	<xsl:template match="lot-line" mode="frames">
		<xsl:if test="position() &lt; $max_frames + 1">
			<frame>
				<xsl:attribute name="width">
					<xsl:value-of select="$frame_width"/>
				</xsl:attribute>
				<xsl:attribute name="height">
					<xsl:value-of select="$frame_height"/>
				</xsl:attribute>
				<xsl:attribute name="x1">
					<xsl:value-of select="$initial_left_pos + ((position()-1) mod $number_columns) * $width_increment"/>
					<xsl:text>cm</xsl:text>
				</xsl:attribute>
				<xsl:attribute name="y1">
					<xsl:value-of select="$initial_bottom_pos - floor((position()-1) div $number_columns) * $height_increment"/>
					<xsl:text>cm</xsl:text>
				</xsl:attribute>
			</frame>
		</xsl:if>
	</xsl:template>

	<xsl:template match="lot-line" mode="story">
		
		<stylesheet>

            		<blockTableStyle id="labelTable">

                		<blockFont name="Helvetica-BoldOblique" size="12" start="0,0" stop="-1,0"/>
                		<lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,0"/>

                		<lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-1"/>
				<lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-2"/>
				<lineStyle kind="BOX" colorName="black" start="0,0" stop="-1,-3"/>
            		</blockTableStyle>

        	</stylesheet>

		<blockTable style="labelTable" colWidths="2.8cm,5.4cm,2.8cm">
		<tr>
			<td><para style="small"><xsl:value-of select="company"/></para></td>
			<td><para style="centered"><xsl:value-of select="creationdate"/></para></td>
			<td><para style="right">Work order: <xsl:value-of select="wo"/></para></td>

		</tr>
		<tr>
			<td>
				<para style="small"><xsl:value-of select="product"/></para>
				<para style="nospace"><b><xsl:value-of select="code"/></b></para>
			</td>
		</tr>
                <tr>
			<td>
				<para style="small">Pallet ID</para>
				<para style="small"><b><xsl:value-of select="serial"/></b></para>			
			</td>
			
			<td><barCode xdim="5cm" ratio="4.0" height="1cm"><xsl:value-of select="code"/></barCode><para style="centered"><xsl:value-of select="code"/></para></td>
		</tr>
		<tr> 
			<td>
				<para style="small">Min. sales Qty</para>
				<para style="nospace"><b><xsl:value-of select="quantity"/></b></para>
			</td>
			<td>
				<para style="small">Pallet Qty</para>
				<para style="nospace"><b><xsl:value-of select="quantity"/></b></para>
			</td>
			<td>
				<para style="small">Final Inspection by</para>
				<para style="nospace"><b><xsl:value-of select="inspector"/></b></para>
			</td>
		</tr>
		<!-- 
		<tr>		
			<td>
				<para>Pallet ID</para><para> <xsl:value-of select="pallet"/> </para>
				
			</td>

			<td>
				<spacer length="0.3cm"/><barCode><xsl:value-of select="serial"/></barCode><para style="nospace">Serial: <xsl:value-of select="serial"/></para><nextFrame/>
			</td>
			
		</tr>
		
		-->
		</blockTable>
		<!-- <nextFrame/>-->
	</xsl:template>
</xsl:stylesheet>
